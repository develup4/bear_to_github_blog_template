---
title:  🤚rvalue reference

subtitle:  너는 왜 혼자 더 복잡해지니
categories: language  
tags: cpp
 
---

  
  
말그대로 `rvalue의 reference`이다. 따라서 일반변수와 같은 lvalue는 참조하지 못한다.  
(나중 universal reference와는 구분한다)  
  
다만 어려워지는 부분은,  
rvalue의 정의가 Modern C++부터 굉장히 복잡해졌다는 점이다.  
(고전적인 rvalue는 prvalue(pure rvalue)로서 하나의 영역에 불과해졌다)  
  
기본적인 사용례를 보면 아래와 같다.  
  
```cpp  
#include <iostream>  
#include <algorithm>  
using namespace std;  
  
int&& foo() { return 10; }  
void f(int&) { cout << "int&" << endl; }  
void f(int&&) { cout << "int&&" << endl; }  
  
int main()  
{  
	int&& rr1 = 10;  
	int&& rr2 = foo();  
	f(10);   
	f(foo());   
	f(rr1);   
	f(rr2);   
  
	int n = 10;  
	f(n);   
	f(static_cast<int&&>(n));   
	f(move(n));   
	return 0;  
}  
```  
  
&& 연산자로 rvalue reference를 정의한다.  
그리고 그 중 rvalue reference로 변환하는 move 함수에 대해 살펴보면,  
  
```cpp  
template <typename T>  
T&& move(T t)  
{  
    return static_cast<T&&>(t);  
}  
```  
  
이 정도로 구현된다고 추측할 수 있다. 즉, 위 예제에서 move 함수 윗 라인과 동일한 것이다.  
move라는 함수의 이름은 관련있는 개념인 이동 생성자와 연관이 있는것으로 보인다.  
  
  
위에서도 잠깐 언급했던 `universal reference`에 대해 살펴보면,  
auto나 template 인자처럼 **type을 추론하는 경우에는 && 연산자가 lvalue와 rvalue를 모두 받을 수 있다.**  
int n = 10;  
auto&& rRef = n;  
  
위와 같이 lvalue를 받는다던지,  
아래 예제에서 주석의 arg처럼 사용이 가능한 것이다.  
  
```cpp  
#include <iostream>  
#include <mutex>  
using namespace std;  
  
void f1(int a) { cout << "f1 : " << a << endl; }  
void f2(int& a) { cout << "f2 : " << a << endl; a = 10; }  
void f3(int&& a) { cout << "f3 : " << a << endl; }  
mutex m;  
  
// arg는 lvalue, rvalue가 모두 가능하다  
template<typename F, typename A> void lockAndCall(F func, A&& arg)  
{  
	lock_guard<mutex> lock(m);  
	func(forward<A&&>(arg));    // perfect forwarding  
}  
int main()  
{  
	int n = 0;  
	lockAndCall(f1, 10);   
	lockAndCall(f2, n);   
	lockAndCall(f3, 10);   
	return 0;  
}  
```  
  
위 예제는 `perfect forwarding`에 대한 예제이기도 한데, 인자로 rvalue reference를 받는 함수에서 받은 인자를 다른 함수에게 rvalue로 전달하는 것을 의미한다.  
  
```cpp  
template<typename F, typename A> void lockAndCall(F func, A&& arg)  
{  
	lock_guard<mutex> lock(m);  
	func(arg);    // why not?  
}  
```  
  
이미 arg가 A&& 타입인데 func에게 그대로 전달하면 안되나? 라고 생각할 수 있지만,  
기억해야 한다.  
  
**이름이 있는 rvalue reference는 lvalue이다.**  
  
arg는 이름이 있는 매개변수이기 때문에 lvalue로 인식된다.  
