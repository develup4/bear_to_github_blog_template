---
title:  CSS selector

categories: CSS 
tags: selector
 
---

  
  
   
선택자 / 스타일 속성 / 스타일 값  
h1 {  
    color : red;  
}  
  
  
*** 전체 선택자** : body보다 넓은 개념  
  
**- Pseudo-class selector**  
:로 확장하는걸 가상클래스 선택자라고 한다.  
  
**- Pseudo-element selector**  
::은 가상요소선택자라고 한다.  
  
**# 아이디 선택자**  
  
**. 클래스 선택자**  
=> 여러개 사용이 가능하다  
<h1 class="aaa bbb">  
  
  
**기본 속성 선택자**  
input[type=text] {  
    background: red;  
}  
  
=> 대괄호안에 속성과 값을 넣어 한정시킬 수 있다.  
  
**후손 선택자**  
말 그대로 자식을 포함해서 더 후손까지 적용시킬 수 있다.  
  
선택자A 선택자B  
=> A의 후손에 위차하는 선택자 B를 선택함  
#header h1 {  
    color:blue;  
}  
  
// 아이디가 header인 태그의 후손인 h1 선택  
  
  
**자손 선택자**  
선택자A > 선택자B  
=> 바로 아래 자손만 적용시킨다.  
  
**동위 선택자**  
선택자A + 선택자B  
=> 바로 뒤에 있는 동위 태그  
  
선택자A ~ 선택자B  
=> 뒤에 위치하는 동위 태그  
  
**반응선택자**  
:active  
:hover  
  
**상태선택자**  
:checked  
:focus  
:enabled  
:disabled  
  
  
**구조선택자**  
유용한 기능이다.  
li:nth-child(2n+1)  
  
<li> 중 저 수열에 해당하는 애들만 적용된다.  
<li>의 자식중이 아니라 <li> 중이라는것을 주의  
   
