---
title:  🦀Rust syntax

subtitle:  복잡하지만 아름답다
categories: language 
tags: rustlang  syntax
 
toc: true
toc_sticky: true
---

  
  
어느 언어를 배우건 기본문법은 비슷하다. Rust도 예외는 아니다.  
그래서 역시나 주의할만한 사항 위주로 간단하게 정리하려한다.  
  
  
## Scala 타입과 Compound 타입  
Rust는 `타입지향적 언어`이며 `scala 타입`과 `compount 타입`이 있다.  
  
`scala`는 다른 언어의 primitive 타입과 의미가 비슷하며 rust가 자동으로 **stack memory**에 할당을 한다.  
`compound`는 tuple이나 array같은 복합체로 **heap memory**에 할당된다.  
  
  
## 변수의 선언 : let과 mut  
```rust  
let a = 5;  
a = 6;    // compile error  
  
let mut b = 5;  
b = 6;    // Okay  
```  
  
`let`은 변경할 수 없는 변수(?)의 선언이다. (const가 상수를 위해서 따로 있다고해서 이상한 설명이 되어버렸다)  
기본적으로 함수형 프로그래밍처럼 **불변성을 기본**으로 하려는 것 같다.  
  
`let`에 `mut`를 붙이면 비로소 변수가 되는데 **mutable**이란 뜻이다.  
정수형의 기본형은 **32bit**로 타입을 언급하지 않는다면 기본적으로 정의된다.  
  
```rust  
let mut a = 2147483647;    // 32bit  
a = a + 1;    // compile error  
```  
  
a는 타입을 정의하지않아 기본인 32bit이다. compile해보면 compiler는 변수의 **overflow나 round robin을 허용하지 않는다.** warning이 아니라 ~compile error~가 발생한다. 매우 엄격하다.  
  
```rust  
let mut a:i64 = 2147483647;  
a = a + 1;    // Okay  
```  
  
변수 뒤에 위와 같이 타입 지정을 할 수 있고 a는 64비트이므로 정상적으로 동작한다.  
  
```rust  
let x = 2.0;    // 64bit  
let y:f32 = 3.0;  
```  
  
반대로 실수형의 경우 64bit가 기본이다.  
C언어에서 double이 기본이고 빠른 것과 비슷해보인다. 컴퓨터공학적으로 당연한 이야기이다.  
  
```rust  
let months = ["Jan", "Feb"];  
println!("{}", months[3]);    // compile error  
```  
  
먼저 설명이 빠진 부분이 있었는데 저 { }는 예상하듯 placeholder이다.  
(like %d in C language)  
그리고 중요한 것은 이 코드는 [3]에서 overflow가 발생하는데 ~compile error~가 발생한다.  
  
즉, **잘못된 memory access를 미리 막는다.**  
  
하면 할수록 문법보다는 rust가 얼마나 엄격한지에 대한 설명이 되어간다.  
하지만 지저분하지않고 모던하다.  
  
  
## 함수  
```rust  
fn main() {  
    another_function(3);  
}  
  
fn another_function(x:i32) -> i32 {  
    println!("x={}", x);  
    x + 1  
}  
```  
  
함수가 미리 앞에 선언될 필요가 없다(모던하지?)  
  
그리고 return value는 마지막은 `expression`이다. ~세미콜론을 까먹은 것이 아니다.~  
(오히려 ;를 붙이면 expression이 아닌 statement가 되어서 에러가 난다)  
  
그리고 물론 다른 언어처럼 명시적으로 return을 쓸수도 있다.  
  
  
## Tuple  
`tuple`은 아래와 같이 사용되며 복합적인 타입이 사용될 수 있다.  
(Modern C++ 등에서도 제공되는 그 tuple이다)  
  
```rust  
fn main() {  
    let x: (i32, f64, u8) = (500, 6.4, 1);  
  
    let five_hundred = x.0;  
    let six_point_four = x.1;  
    let one = x.2;  
}  
```  
  
그리고 배열,  
```rust  
fn main() {  
    let a = [1,2,3,4,5];  
    for element in a.iter() {  
        if element == 3 {  
            break;  
        }  
    }  
}  
```  
  
배열에는 method인 `iter()`가 있음과 if, while 등의 조건에는 괄호가 없음을 주목하자.  
(있으면 오히려 warning이 난다)  
  
왜냐면 여기서 if는 **expression**이다. 따라서 let과 함께 아래처럼 사용할 수 있다.  
  
```rust  
let number = if condition {  
        5  
    } else {  
        6  
    };  
```  
  
삼항연산자보다 더 깔끔해보인다.  
expression의 개념을 알아보기 위해 예제를 하나 더 살펴보자.  
  
``` rust  
fn main() {  
    let x = 5;  
  
//    let x = (let y = 6); // compile error  
  
    let y = {  
        let x = 3;  
        x + 1  
    };  
  
    println!("The value of y is: {}", y);  
}  
```  
  
  
## 구조체…사실은 클래스  
이번에는 구조체를 알아본다.  
(method도 있으니 사실상 클래스다)  
  
```rust  
fn main() {  
    struct User {  
        username: String,  
        email: string,  
        sign_in_count: u64,  
        active: bool  
    }  
  
    impl User {  
        fn get_active(&self) -> bool {     // first parameter must be &self  
            self.active  
        }  
    }  
  
    let user1 = User {  
        email: String::from("example@xyz.com");  
        username: String::from("hoo");  
        active: true,  
        sign_in_count: 1  
    };  
  
    let user2 = User {  
        active: false,  
        ..user1    // email, username => move from user1  
    }  
  
    println!("{}", user1.email);    // compile error => user1.email move  
}  
```  
  
method의 첫번째 인자로 `&self`를 받는 점  
(C++의 this와 같다. 여러모로 C++ 유저가 파악하기 쉬운 언어같다)  
  
method가 impl로 따로 떨어져있는 점  
(C++에서 선언과 구현을 나누는 것과 유사해보인다. data structure만 깔끔하게 따로 볼 수 있다)  
