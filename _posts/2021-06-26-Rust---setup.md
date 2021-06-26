---
title:  Rust - setup

categories: rustlang

tags: 
---

  
   
설치는 아래 경로에 나온대로 Easy하게 진행이 가능하다.  
![]({{ site.url }}{{ site.baseurl }}/assets/images/2021-06-26-Rust - setup/dthumb-phinf.pstatic.net.jpg)이미지 썸네일 삭제  
  
**Install Rust**  
A language empowering everyone to build reliable and efficient software.  
www.rust-lang.org  
  
* 오른쪽 정렬오른쪽 정렬왼쪽 정렬왼쪽 정렬가운데 정렬가운데 정렬  
  
*   
  
* 삭제삭제  
각 운영체제에 맞게 Terminal 혹은 설치파일로 진행할 수 있으며,  
나는 제약사항 때문에 윈도우에서 msi 파일을 통해서 설치를 진행하였다.  
  
Windows의 경우, compile시 아래와 같은 에러가 날 수 있기 때문에,  
(Visual Studio가 설치되어있지 않다면)  
error: linker `link.exe` not found  
note: The system cannot find the file specified. (os error 2)  
note: the msvc targets depend on the msvc linker but `link.exe` was not found  
note: please ensure that VS 2013, VS 2015 or VS 2017 was installed with the Visual C++ option  
error: aborting due to previous error  
  
아래 링크에서 Visual C++ 개발도구를 설치하면 문제가 없다.  
https://visualstudio.microsoft.com/ko/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16  
  
  
rust를 설치하면 cargo라는 Package Manager가 같이 설치되는데,  
터미널에서 아래 키워드로 설치여부를 확인해보자.  
> cargo —version    
  
  
Cargo는 프로젝트 관리, 패키지 관리, 배포, 버전관리 등 여러가지 기능을 해주는데,  
C나 C++처럼 low level을 다루는 언어인데 Web 기술마냥 사용할 수 있다는 점이 굉장히 인상적이었다.  
  
카고는 러스트의 빌드 시스템이자 패키지 관리자입니다.  
카고는 러스트 코드의 빌드, 의존 라이브러리(dependencies) 다운로드 및 빌드 등을 대신 수행합니다.  
  
Cargo는 기본적으로 4가지의 일을 한다  
1. 프로젝트의 정보들을 두 개의 메타데이터 파일로 볼 수 있다.  
2. 프로젝트 의존성을 가져오고 빌드한다.  
3. 프로젝트가 올바르게 빌드 될 수 있도록 rustc혹은 다른 컴파일러의 인자를 맞춰 실행시켜준다.  
4. 규칙에 대해 설명해주고 작업공간을 만들어 Rust project를 더 쉽게 할 수 있도록 해준다  
  
출처: https://jen6.tistory.com/86 [./make all]  
  
  
그럼 간단하게 프로젝트를 만들어서 Hello World를 만들어보자.  
> cargo new {Project명} —bin    
  
터미널에서 위와 같이 프로젝트를 생성하면, 현재경로에 프로젝트 폴더가 생긴다.  
프로젝트 폴더에는 매니페스트 파일인 Cargo.toml  
.gitignore  
src 폴더 등이 있으며,  
  
src에는 main.rs라는 소스코드와  
fn main() {  
    println!("Hello World");  
}  
  
헬로우월드 코드가 이미 구현되어 있다.  
  
첫 코드이니 간단한 설명을 하자면,  
println!의 느낌표는 매크로라는 뜻이다. 나중에 알아본다.  
  
intent는 탭이 아닌 스페이스바 4번으로 규칙이 정해져있으며,  
snake case convention rule을 사용한다. 즉, 소문자와 언더스코어를 조합한 방식이다.  
임베디드같아서 싫지만 타이핑이 훨씬 쉽고, 한결같기만하다면 사실 어떤 방식이든 이쁜 것 같다.  
  
이제 rs 파일을 컴파일해보자.  
(당연하게도 컴파일 언어이다)  
> rustc .\main.rs    
  
실행시 컴파일에러가 없다면 exe 파일이 생성되고(윈도우의 경우),  
exe 파일을 실행하면 Hello World가 출력된다.  
  
이것은 rust의 기본 컴파일 방식이고,  
Cargo를 통해서 더 편하게 진행이 가능하다.  
  
프로젝트 폴더 경로에서,  
> cargo build    
  
를 진행하면 target 폴더에 산출물(exe등) 이 나오게 된다.  
  
그 외에도,  
> cargo check    
  
이것은 컴파일을 하되 실행파일을 생성하지 않기때문에 빠르며, 컴파일 가능여부만을 파악하기에 좋다.  
  
> cargo run    
  
그리고 가장 많이 사용하는 이 명령은 컴파일 및 실행을 동시에 진행해준다.  
   