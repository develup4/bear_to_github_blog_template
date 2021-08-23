# 🐭Goroutine
## 흑마법사가 되어보자
### 2021-06-24
#language #golang #goroutine

![](%F0%9F%90%ADGoroutine/img.png)

드디어 Golang을 배우는 가장 큰 이유인 고루틴(Goroutine) 소개이다.
노마드코더 사이트의 go 언어 강좌를 통해 공부하였다.

## 한번 사용해보자
```go
func sexyCount(person string) {
	for i := 0; i < 10; i++ {
		fmt.Println(person, “is sexy”, i)
		time.Sleep(time.Second)
	}
}

func main() {
	go sexyCount(“nico”)
	sexyCount(“flynn”)
}
```

두 번의 sexyCount 호출이 있는데 동시에 실행이 된다.

`go`만 앞에 붙이면 `concurrenncy`하게 돌아가는 것이다.
골때린다 정말…

```go
func main() {
	go sexyCount(“nico”)
	go sexyCount(“flynn”)
}
```

이렇게 하면?
아무출력 없이 프로그램이 끝나버린다.

**main함수는 goroutine을 기다리지 않는다!**

어찌되었건 전체 흐름은 있어야하는 것이다.

```go
go sexyCount(“nico”)
go sexyCount(“flynn”)
time.Sleep(time.Second * 5)
```

이런식으로 sleep을 해보면 잘돌아간다.

## Channel
다음은 Channel개념이다.

`channel`은 `goroutine`과 `main 함수` 사이에 정보를 전달하기 위한 방법이다.

결국 멀티코어로 멀티쓰레드를 돌린다는 것은 **결과를 취합하는 일**이 생기게 되어 있다.
그럴 때를 위해 존재하는 것이 채널이다.

혹은 `goroutine`과 `goroutine` 사이에 통신을 위해서도 쓰일 수 있다.
보통의 멀티쓰레드 프로그래밍이라고 생각한다면 이런일을 하기위해 아주 큰 노력이 들것이다.
(C++로 한다고 생각을 해보자…)

```go
func main() {
	c := make(chan bool)        // 1. 채널을 만든다 c는 채널의 이름이다
	people := [2]string{“nico”, “flynn”}
	for _, person := range people {
		go isSexy(person, c)    // 2. 고루틴의 인자로 채널을 넘겨준다
	}
	fmt.Println(<-c)    // 5. <- 연산자로 채널로부터 값을 받는다. 그리고 받을때까지 대기한다. sleep 필요없다.
	fmt.Println(<-c)    // <-를 쓰면 이 문장은 블로킹연산이 된다.
	fmt.Println(<-c)    // 고루틴은 두개가 도는데 3개의 채널을 기다리므로 데드락으로 프로그램이 죽는다.
}

func isSexy(person string, c chan bool) {    // 3. 채널을 받을 수 있도록 파라메터를 추가한다
	time.Sleep(time.Second * 5)
	fmt.Println(person)
	c <- true      // 4. 채널로 값을 준다. 리턴같은 개념이다.
}

result := <-c;
```

`:= <-`라니…뭔가 고대문자스럽지만 저것이 결과를 취합받기 위한 코드이다.
기괴하다고 생각하지말고 귀엽다고 생각을 해보자(..)


`func hitURL(url string, c chan<- result) `

여기서 `chan<-` 이 의미는 채널을 통한 sendOnly라는 뜻이다.
hitURL에서는 채널을 통해 데이터를 받을수는 없다. 화살표가 오른쪽인지 왼쪽인지를 구분하자.