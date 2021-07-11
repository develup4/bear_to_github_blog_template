---
title:  ECMA6 - spread

categories: language 
tags: javascript  es6
 
---

  
  
   
구성요소를 풀어헤치는 기능을 spread라고 한다.  
const friends = [1, 2, 3, 4];  
const family = ["a", "b", "c"];  
  
console.log([…friends, …family]);  
  
  
두 배열의 구성요소를 합쳤다. 다만 새로운 배열을 만드는 것이기때문에 다른 오브젝트이며 참조가 다르다.  
  
const sexy = {  
  name: "nico",  
  age: 24  
}  
  
const hello = {  
  sexy: true,  
}  
  
console.log({…sexy, …hello});  
  
이렇게 객체에 이용할 수도 있다. 두 객체의 구성요소를 모두 가지는 새로운 객체가 만들어졌다.  
  
const friends = [1, 2, 3, 4];  
const newFriends = […friends, 5];  
  
이렇게 구성요소를 추가할수도 있지만 기존 friends에는 변화가 없고 새로운 배열이 만들어진다는 것을 주의하자  
  
const nico = {  
  username: "nico"  
};  
  
console.log({…nico, password: 123 });  
  
이렇게 객체의 구성요소를 추가할수도 있다.(역시 추가가 아니라 생성이지만)  
  
const lastName = prompt("Last name");  // 콘솔에서 입력받음  
  
const user = {  
  username: "nico",  
  age: 24  
  …(lastName !== "" && lastName)    // optional  
};  
  
optional field를 추가하고 싶다면?  
저렇게 조건식으로 spread를 하면 안의 내용에 따라 lastName 필드가 없을수도 있다.  
   
