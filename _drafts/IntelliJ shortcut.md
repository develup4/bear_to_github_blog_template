# IntelliJ shortcut
#shortcuts #intellij
### 메인메소드 생성

- `COMMAND + 1`을 누르면 좌측의 프로젝트 파일 트리로 focus된다.
- `COMMAND + N`을 누르면 **현재 선택된 위치에서** 생성할 수 있는 종류(Java class, Package, …)가 나온다. 예를 들어 프로젝트 root에서는 생성목록에 Package가 없는데, 디렉토리에서 해당 단축키를 누르면 Package도 나온다.

![](IntelliJ%20shortcut/34BD35F8-BE30-49F2-873F-5E07A1D86BCF.png)
![](IntelliJ%20shortcut/9B612DC0-E1A3-452B-8033-282866415B9E.png)

> 디렉토리 추가시 `Src/main/java`  
> 이런식으로 슬래시로 구분해서 만들면 hierarchy대로 디렉토리를 만들어 준다.  


- 라이브 템플릿(코드 템플릿) : 자주쓰는 함수에 대한 축약어
**중요!** Command + j를 치면 현재 사용 가능한 축약어가 모두 나온다.

> `psvm` : public static void main(String[] args)  
> `sout` : System.out.println()   
> `soutv` : 지역변수 등의 출력 포맷 제공  
> `soutm` : 메소드명 출력 포맷 제공  
> `soutp` : 파라메터 출력 포맷 제공  

```java
System.out.println();   // sout
System.out.println("this = " + this);   // soutv
System.out.println("HelloServlet.service"); // soutm
System.out.println("req = " + req + ", resp = " + resp);    // soutp
```

- 라이브 템플릿은 설정에서 만들 수 있다.
- 스프링강의에서 tdd를 만들었던것 참고
- 아직 활용 많이 안한 템플릿도 있다 ifn 탭을 치면 특정 변수에 대해 if (var == null) { 형태 만들어줌

@Repository
@RequireArgConstructor
@Transaction
예컨데 이런거 묶어서 하나 만들수도 있겠지


### 메인메소드 실행

- `CONTROL + SHIFT + R` : 현재 포커스된 파일에서의 main  메소드를 실행
- `CONTROL + R` : 이전에 실행했던 main 메소드를 실행 (다른 파일을 보고 있을때 활용할 수 있다)



### 라인 수정하기

- `COMMAND + D` : 현재 커서가 있는 라인을 복제하여 아래줄에 추가한다
- `SHIFT + DELETE` : 현재 라인을 삭제한다

- `CONTROL + SHIFT + J` : 여러 라인의 문자열 합치기

```java
String query = "SELECT *  "  // 여기 커서를 두고 단축키를 두 번 실행
        + "FROM member "
        + "WHERE member.name = 'ksh'";

// 실행 결과
String query = "SELECT * FROM member WHERE member.name = 'ksh'";
```

- `OPTION + SHIFT + 방향키` : 라인을 이동시킨다
- `COMMAND + SHIFT + 방향키` : 구문 안에서만 라인을 이동시킨다. 특별한 일이 없다면 권장되는 사항.

- `OPTION + SHIFT + COMMAND + 좌우 방향키` : 엘리먼트 단위로 옮기기

```html
<h1 id="title" name="name">

// 실행결과
<h1 name="name" id="title">
```

```java
private void print(HttpServletRequest req, HttpServletResponse resp)

// 실행결과
private void print(HttpServletResponse resp, HttpServletRequest req)
```



### 코드 즉시보기

- `COMMAND + P` : 파라메터 확인하기

![](IntelliJ%20shortcut/53072151-F2D8-4C13-BE99-01ADE4FC3343.png)

- `OPTION + SPACE` : 선언부를 즉시 확인
![](IntelliJ%20shortcut/EB2A31DE-FA85-421C-B62E-D71F20B1F49E.png)

- `F1` : Javadoc 확인
- 
![](IntelliJ%20shortcut/F5AAC78C-4DB3-4F62-B957-64C511EC61AA.png)



### Search 기능
command d 단축키 힛ㅡ토리 코드 포함해서 포스팅 주석간것들도
Command + O로 검색가능하고 all에서는 라이브러리까지 다 된다. 스프링까지. Bean factory 이런것도 막 검색해서 들어가서 다 볼 수 있음
아니다 걍 쉬프트 두번

- Command + F: 검색
- Command + R : replace
- Command + Shift + F :  프로젝트 전체에서 검색, 전체에서 교체도 가능

- Command + Shift + O : 파일검색 원하는 파일 열기
- => 동일한 이름 파일이 많을때 {패키지명}/{파일명} 이렇게 검색하면 된다.
- Command + Option + O : 원하는 심볼(메서드명이라던지) 검색

- Command + Shift + A : 인텔리제이 액션 검색 => 원하는 기능 메뉴 안가고도 찾을수 있다. => 매우 중요!

- Command + E : 최근 열었던 파일들이 팝업으로 나온다
- Command + Shfit + E : 최근 수정한 파일만 나온다.


### 포커스 기능
- Option + 방향키 : 단어단위로 이동
- Shift + Option + 방향키: 단어단위로 선택
- fn + 방향키 : home/end같은 기능. 맥 노트북만 사용할때 유용할듯
- shift + fn+ 방향키: 위에꺼 선택까지
- fn + 위아래 : 페이지 업다운같은 기능
- shift + enter : 커서가 중간에 있어도 그냥 아래줄에 빈줄만들고 내려감

- Option + 방향키 위 : 한단어 선택, 계속 반복하면 점점 늘어남. 단순 단어단위로 늘어나는게 아니라 파라메터면 파라메터 다음꺼, 파라메터가 다 선택되면 함수 전체 이런식으로 계속 의미적으로 늘어남
- Option + 방향키 아래: 위에서 선택한거의 반대로 범위가 줄어듬

- Command + { : 이전 포커스(전에 마우스로 찍었던)로 돌아감
- Command + } : 원래 포커스로 돌아감

- 멀티포커스 : vscode에서 쓰던 그 좋은 기능이다.
```java
public void save(Order order) {
    entityManager.persist(order);
    entityManager.persist(order);
    entityManager.persist(order);
    entityManager.persist(order);
}
```
이런 코드에서 persist를 다 save로 바꾸고 싶다면
persist위에서 옵션키를 두번 누른 상태에서 방향키를 아래로 누르면 계속 커서가 늘어난다.

- f2 => 오류가 난곳으로 포커스 이동



### 자동완성 기능
- Shift + Control +  Space: 사용가능한 것만 보여주는 스마트 자동완성 기능
- static 함수 자동완성 => 스태틱함수는 일반 자동완성으로 안뜬다. control + space 두번 => 근데 스포트라이트 뜨는데?

- 파일 생성때 썼던 COMMAND + N을 클래스 내에서 누르면 자동 생성가능한 목록이 나온다. 생성자 게터 세터 등등
![](IntelliJ%20shortcut/A5CCC4B4-C68E-4C4C-B624-57B02042A9D2.png)

- 오버라이딩 단축키
`CONTROL + O` : Class 안에서  control + o 누르면 오버라이드 목록뜸
CONTROL + I : 추상클래스를 상속할때 implement해야될 메소드들 자동생성

### 리팩토링 기능

- Extract variable
```java
System.out.println(String.format("%d + %d", 1, 2));
System.out.println(String.format("%d + %d", 1, 2));
```
저 인자 두개를 따로 변수로 뽑아내고 싶을때,
일단 대충 옵션 + 화살표 위로하면 적절한 범위를 쉽게 세팅할 수 있을것이다. 그다음에
Command + Option + V를 누르면 위에 두개를 모두 바꿀건지 창이 뜨는데 선택 후 엔터를 치면,

```java
String format = String.format("%d + %d", 1, 2);
System.out.println(format);
System.out.println(format);
```
이렇게 뽑혀나온다.


- Extract parameter
```java
void extractParam(int x) {
	System.out.println(10);
	System.out.println(10);
}
```
만약에 저 10이 인자로 들어온 x라서 변경을 하고 싶다면
Command + Option + P를 눌러서 변경할 수 있다.

```java
void extractParam(int x) {
	System.out.println(x);
	System.out.println(x);
}
```

Command option m : extract method
특정영역 선택해서 메소드로 뽑을 수 있다. 굉장히 많으 쓴다.

밑에 이거는 단축키가 뭔지 모르겠
```java
int count = prototypeBean.getCount(); // 여기서 단축키 실행
return count;
```

```java
return prototypeBean.getCount();
```
(Cleancode에서도 이런 형태로 줄이는게 낫다고 한다. 임시변수 극혐하는듯.



- inner class를 외부로 뽑아내는 기능 : f6


- 이름변경(변수, 클래스, 필드 등등) :  Shift + F6
- 타입 변경 :  Command + Shfit + F6
```java
private String calculate() { return "1"; }
String num = calculate();

=>

private Integer calculate() { return 1; }	// 리턴의 값은 직접 변경해야 한다.
Integer num = calculate();
```


- CONTROL + OPTION + O : 사용하지 않는  import 제=> 근데 optimize imports 액션을 찾아서 on으로 바꾸면 단축키없이도 그냥 알아서 해준다


- COMMAND + OPTION + L : 정렬(포맷팅)







- `CONTROL + T` : 함수내에서 블록지정해서 컨트롤 티 누르고 extract method로 하면 다른 함수로 뽑아내고 호출하는걸로 변경 가능


- option command v : memberRepository.findAll() 이렇게 있을때 누르면, List<Member> all = 이 앞에 붙고 커서도 all 앞에 붙는다.

iter를 치면 그안에 지역변수 포문생성
뭐.iter를 치면 그거 포문생성

쉬프트 에프육 => 클래스명변경하고 파일명도 같이 바꿔줌


```java
memberRepository.save(member);
=> 여기서 커맨드 옵션 브이를 누르면 아래처럼 변수로 뽑느다

long save = memberRepository.save(member);



2.
List<Member> result = entityManager.createQuery("select m from Member m", Member.class).getResultList();
return result;	// 여기서 커맨드 옵션 n을 누르면 합친다.

=>
return entityManager.createQuery("select m from Member m", Member.class).getResultList();


```

Control + Control : 어떤 동작도 하는 창 열림
Shift + Shift : 통합검색창



## 디버그
- CONTROL + SHIFT + D : 현재 포커스에 있은 함수를 디버그 모드로 실행
- CONTROL + D : 이전 포커스에 있던 함수 디버그 모드로 실- OPTION + COMMAND + R : 브레이크포인트 걸린상태에서 리- F7 : Step In- F8 : Step over
- SHIFT + F8 : Step out => 잘안쓰던건데 유용하네. 스텝인투했다가 바로 나가서 다음줄에서 멈추는 기능

> 브레이크 포인트에서 마우스 오른쪽을 눌러서 조건을 설정할 수 잇다!  


> Evaluate  
> OPTION  + F8  
> 이클립스에서 쓰던 평가식이다. 복잡한 현재 상태를 확인할 수 있다.  




## GIT 메뉴
상단 View - Tool window - git으로 창 열수있
코드상에서 CONTROL + V를 누르면 깃 팝업창이 뜬다. 보통 이걸 통해 필요한걸 연다.
팝업창 앞에 번호가 있는데 번호를 누른다.
- COMMAND + D :  diff 보기
- COMMAND + K : COMMIT
(체크박스로 다양한 옵션들이 있다. 반영전 포맷팅하는 기능도 있다)
-  COMMAND + SHIFT + K : PUSH
- PULL은 단축키가 없다. 액션 검색에서 git pull을 검색하는게 편하다.