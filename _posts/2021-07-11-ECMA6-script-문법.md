---
title:  ECMA6 script 문법

categories: Javascript 
tags: ES6
 
---

  
  
   
Generator  
  
  
Function* listPeople() {  
Yeild "dal";  
Yeild "flynn";  
}  
  
Const list = listPeople();  
List.next();  
List.next();  
  
=> 더정리필요  
  
  
Proxy => c#의프로퍼티같은 기능이다(setter/getter)  
이것도 블로그정리  
  
  
  
?? 연산자  
Nullish coalescing operator  
  
Let name;  
Name || "hello"  
근데 이 용법은 기본적으로 boolean체크라서 name=0이면 값도 0이라 있는데도 헬로우가 출력된다 이럴때 ?? 사용  
  
  
  
  
옵셔날 체이닝(리액트에서 무지 유용)  
If (lyyn.profile && lynn.profile.email && lynn.profile.email.provider)  
  
  
===  
  
  
If (lynn?.profile?.email?.provider)  
  
  
  
  
  
  
String(minutes).padStart(2,"0);  
Minutes를 두자리수 빈곳은 패딩 0으로 출력  
=>"03"  
  
Padend도있음  
기존 변수 수정이 아닌 결과만 출력임을 주의  
  
  
  
  
  
Trimstart, trimEnd()  
=>각각 앞뒤에 빈공간 제거  
기존Trim은 양쪽다제거했는데 필요에따라 사용가능하고 이것도 결과만 바뀌지 변수 안바뀜  
  
  
  
  
Object.value(어떤오브젝트)  
=> 오브젝트의 값들만 배열로 반환  
  
Object.entries(어떤 오브젝트)  
배열의 배열 리턴  
[["name", "a"], ["age",2]]  
필드와 값이 다 있어서 foreach같은걸로 출력하기도 쉽고 활용가능  
  
  
Object.fromEntities()  
=>다시 오브젝트로 만들어줌(시리얼라이즈 용도로 가능할까?)  
  
  
  
Array.flat()  
Flatten이라는 라이브러리 이제 안써도 됨  
인자로 풀어해질 배열의 뎁스 입력받음  
  
  
Promise.all()은모두 성공해야 성공인데  
Promise.allSettled는일부만 성공해도 진행한다. 예외가 있건 없건 끝까지 진행해서 끝나기만하면 된다.  
  
먼저 함수의 앞에async라는예약어를 붙입니다 그리고 나서 함수의 내부로직 중 http통신을 하는 비동기 앞에 awiat를붙입니다. 여기서 주의할점은 비동기 메서드가 꼭 프로미스 객체를 반환해야 어웨이트가 의도한대로 동작합니다.  
   
  
  
  
for (const friend of friends) {  
  if (friend === "Dal") break;  
  console.log(friend);  
}  
이런식으로 쓰는것을 for of라고 한다.  
다른언어의 foreach와 흡사하다.  
   
forEach와는 달리 break가 가능하고 위에 const friend 대신 let friend도 가능하다(바람직하지는 않겠지)  
그리고 결정적으로 iterable한 여러가지에 사용이 가능하다.  
nodelist, string, array 등등  
만약 위에서 friends가 문자열 "abcd"였다면 한글자씩 출력됐을 것이다.  
  
