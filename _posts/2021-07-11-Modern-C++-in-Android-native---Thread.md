---
title:  Modern C++ in Android native - Thread

categories: C++ 
tags: Android  Thread
 
toc: true
toc_sticky: true
---

  
  
   
#include <stdio.h>  
#include <pthread.h>  
#include "StrongPointer.h"  
#include "RefBase.h"  
  
using namespace android;  
  
  
void *foo(void* data)  
{  
	printf("foo()\n");  
	return 0;  
}  
  
int main()  
{  
	pthread_t thread;  
	pthread_create( &thread, 0, foo, 0 );  
	pthread_join( thread, 0 );  
	return 0;  
}  
  
  
Android는 Linux 위에 올라가 있으므로 리눅스에서의 쓰레드부터 살펴보면,  
기본적인 POSIX thread는 위와 같이 사용한다.  
#include <stdio.h>  
#include <pthread.h>  
#include "StrongPointer.h"  
#include "RefBase.h"  
  
using namespace android;  
  
class Thread  
{  
	pthread_t thread;  
public:  
	virtual void foo(void) = 0;  
	static void *_foo(void* data)  
	{  
		Thread *self = static_cast<Thread*>(data);  
		self->foo();  
		return 0;  
	}  
	void run() { pthread_create( &thread, 0, _foo, this ); }  
	void join() { pthread_join( thread, 0 ); }  
};  
  
class MyThread : public Thread  
{  
public:  
	void foo(void)  
	{  
		printf("MyThread::foo()\n");  
	}  
};  
  
int main()  
{  
	MyThread thread;  
	thread.run();  
	thread.join();  
	return 0;  
}  
  
이것을 클래스로 wrapping하면 이렇게도 쓸 수 있을것이다.  
마찬가지로 Android에서도 POSIX thread를 wrap해서 구현해놓았는데,  
#ifndef _LIBS_UTILS_THREAD_H  
#define _LIBS_UTILS_THREAD_H  
  
#include <stdint.h>  
#include <sys/types.h>  
#include <time.h>  
  
#if !defined(_WIN32)  
# include <pthread.h>  
#endif  
  
#include "Condition.h"  
#include "Errors.h"  
#include "Mutex.h"  
#include "RefBase.h"  
#include "Timers.h"  
#include "ThreadDefs.h"  
  
// —————————————————————————————————————  
namespace android {  
// —————————————————————————————————————  
  
// DO NOT USE: please use std::thread  
  
class Thread : virtual public RefBase  
{  
public:  
    // Create a Thread object, but doesn’t create or start the associated  
    // thread. See the run() method.  
    explicit            Thread(bool canCallJava = true);  
    virtual             ~Thread();  
  
    // Start the thread in threadLoop() which needs to be implemented.  
    // NOLINTNEXTLINE(google-default-arguments)  
    virtual status_t    run(    const char* name,  
                                int32_t priority = PRIORITY_DEFAULT,  
                                size_t stack = 0);  
      
    // Ask this object’s thread to exit. This function is asynchronous, when the  
    // function returns the thread might still be running. Of course, this  
    // function can be called from a different thread.  
    virtual void        requestExit();  
  
    // Good place to do one-time initializations  
    virtual status_t    readyToRun();  
      
    // Call requestExit() and wait until this object’s thread exits.  
    // BE VERY CAREFUL of deadlocks. In particular, it would be silly to call  
    // this function from this object’s thread. Will return WOULD_BLOCK in  
    // that case.  
            status_t    requestExitAndWait();  
  
    // Wait until this object’s thread exits. Returns immediately if not yet running.  
    // Do not call from this object’s thread; will return WOULD_BLOCK in that case.  
            status_t    join();  
  
    // Indicates whether this thread is running or not.  
            bool        isRunning() const;  
  
#if defined(__ANDROID__)  
    // Return the thread’s kernel ID, same as the thread itself calling gettid(),  
    // or -1 if the thread is not running.  
            pid_t       getTid() const;  
#endif  
  
protected:  
    // exitPending() returns true if requestExit() has been called.  
            bool        exitPending() const;  
      
private:  
    // Derived class must implement threadLoop(). The thread starts its life  
    // here. There are two ways of using the Thread object:  
    // 1) loop: if threadLoop() returns true, it will be called again if  
    //          requestExit() wasn’t called.  
    // 2) once: if threadLoop() returns false, the thread will exit upon return.  
    virtual bool        threadLoop() = 0;  
  
private:  
    Thread& operator=(const Thread&);  
    static  int             _threadLoop(void* user);  
    const   bool            mCanCallJava;  
    // always hold mLock when reading or writing  
            thread_id_t     mThread;  
    mutable Mutex           mLock;  
            Condition       mThreadExitedCondition;  
            status_t        mStatus;  
    // note that all accesses of mExitPending and mRunning need to hold mLock  
    volatile bool           mExitPending;  
    volatile bool           mRunning;  
            sp<Thread>      mHoldSelf;  
#if defined(__ANDROID__)  
    // legacy for debugging, not used by getTid() as it is set by the child thread  
    // and so is not initialized until the child reaches that point  
            pid_t           mTid;  
#endif  
};  
  
}  // namespace android  
  
// —————————————————————————————————————  
#endif // _LIBS_UTILS_THREAD_H  
// —————————————————————————————————————  
  
이것저것 구현사항은 많지만, 기본적인 동작은 인터페이스만 봐도 짐작할 수 있다.  
주의할만한 사항은 쓰레드 객체를 내부에서 strong pointer로 만든 뒤, refCount를 자체적으로 1 감소시킨다는 점이다.  
그래서 일반 포인터로 Android 쓰레드를 사용하면 정상적으로 돌지않는다  
(refCount가 0이 되어버리므로)  
  
즉, 반드시 sp를 써서 사용해야한다.  
as below  
  
using namespace android;  
  
class MyThread : public Thread  
{  
public:  
	bool threadLoop()  
	{  
		printf("MyThread::foo()\n");  
		sleep(2);  
		return true;  
	}  
};  
  
int main()  
{  
	sp<Thread> thread = new MyThread;  
	thread->run("MyThread");  
	thread->join();  
	return 0;  
}  
  
  
  
다음으로 살펴볼 내용은 Android에서 제공하는 Mutex이다.  
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;  
int sum = 0;  
  
class MyThread : public Thread  
{  
public:  
	bool threadLoop()  
	{  
		int local;  
		for(int i=0; i<10000000; i++)  
		{  
			pthread_mutex_lock(&mutex);  
			local = sum;  
			local = local + 1;  
			sum = local;  
			pthread_mutex_unlock(&mutex);  
		}  
				  
		return false;  
	}  
};  
  
int main()  
{  
	sp<Thread> thread1 = new MyThread;  
	thread1->run("MyThread1");  
	sp<Thread> thread2 = new MyThread;  
	thread2->run("MyThread2");  
  
	thread1->join();  
	thread2->join();  
	printf("sum = %d\n", sum );  
	return 0;  
}  
  
역시나 POSIX mutex부터 살펴보면 위와 같이 사용한다.  
  
using namespace android;  
  
Mutex mutex;  
int sum = 0;  
  
class MyThread : public Thread  
{  
public:  
	bool threadLoop()  
	{  
		int local;  
		for(int i=0; i<10000000; i++)  
		{  
			mutex.lock();  
			local = sum;  
			local = local + 1;  
			sum = local;  
			mutex.unlock();  
		}  
				  
		return false;  
	}  
};  
  
그리고 더 편하게 사용하기 위해 역시나 Android에서 wrapper 클래스를 제공하는데,  
다만…여기서 주의할 사항이 있다.  
  
이 임계영역(Critical section)에서 예외발생시 unlock이 안되는 문제가 있을 수 있는것이다.  
그렇다고 모든 catch에서 unlock을 하는 것도 뭔가 불합리하다.  
  
그래서 Android에서 autolock이라는 것을 제공을 한다.  
이것도 역시 RAII 개념이다.  
(자원의 관리는 객체로 한다)  
  
Mutex mutex;  
int sum = 0;  
  
class MyThread : public Thread  
{  
public:  
	bool threadLoop()  
	{  
		int local;  
		for(int i=0; i<10000000; i++)  
		{  
			Mutex::Autolock ll(mutex);  
			local = sum;  
			local = local + 1;  
			sum = local;  
		}  
				  
		return false;  
	}  
};  
  
Autolock은 예외가 발생하더라도 자동으로 unlock을 해준다.  
(call stack에 안남나…?)  
  
  
이번엔 Conditional에 대해 알아보자.  
  
일반적인 생산자 소비자 모델이 있을때 각각이 별개의 쓰레드에서 동작한다면,  
생산도 안했는데 소비자가 작동하는 문제가 있을 수 있다. 일의 순서가 있는 것이다.  
  
이런 문제를 위해 POSIX는 pthread_cond_wait, pthread_cond_signal 등의 api를 제공한다.  
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;  
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;  
  
class Producer: public Thread  
{  
public:  
	bool threadLoop()  
	{  
		pthread_mutex_lock(&mutex);  
		for(int i=0; i<3; i++)  
		{  
			sleep(1);  
			printf("생산중…\n");  
		}  
		printf("생산완료\n");  
		pthread_cond_signal(&cond);  
		pthread_mutex_unlock(&mutex);  
				  
		return false;  
	}  
};  
class Consumer : public Thread  
{  
public:  
	bool threadLoop()  
	{  
		pthread_mutex_lock(&mutex);  
		pthread_cond_wait(&cond, &mutex);  
		for(int i=0; i<3; i++)  
		{  
			sleep(1);  
			printf("소비중…\n");  
		}  
		printf("소비완료\n");  
		pthread_mutex_unlock(&mutex);  
				  
		return false;  
	}  
};  
  
int main()  
{  
	sp<Thread> pro = new Producer;  
	pro->run("Producer");  
	sp<Thread> con = new Consumer;  
	con->run("Consumer");  
  
	pro->join();  
	con->join();  
	return 0;  
}  
  
  
그리고 역시나 Android에서 제공하는 class가 존재한다.  
using namespace android;  
  
Mutex mutex;  
Condition cond;  
class Producer: public Thread  
{  
public:  
	bool threadLoop()  
	{  
		Mutex::Autolock ll(mutex);  
		for(int i=0; i<3; i++)  
		{  
			sleep(1);  
			printf("생산중…\n");  
		}  
		printf("생산완료\n");  
		cond.signal();  
				  
		return false;  
	}  
};  
class Consumer : public Thread  
{  
public:  
	bool threadLoop()  
	{  
		Mutex::Autolock ll(mutex);  
		cond.wait(mutex);  
		for(int i=0; i<3; i++)  
		{  
			sleep(1);  
			printf("소비중…\n");  
		}  
		printf("소비완료\n");  
				  
		return false;  
	}  
};  
  
특이한 점은 signal()과 broadcast()가 있다는 점이다.  
broadcast API는 여러 쓰레드에게 신호를 보낼 수 있어 편리하다.  
   
