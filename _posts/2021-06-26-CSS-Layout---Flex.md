---
title:  CSS Layout - Flex

categories: CSS 
tags: Flex  layout
 
---

  
  
   
Flex Box 이전의 방식은 아래와 같았다.  
<div class="box"></div>  
<div class="box"></div>  
<div class="box"></div>  
  
// 이녀석은 block이다.  
// block은 element이고 block 옆에는 어떠한 엘리먼트도 기본적으로는 올 수 없다.   
.box {      
    backgrouhd: blue;  
    width: 100px;  
    height: 100px;  
    display: inline-block; // 위 박스가 가로로 배열된다  
    // display: inline;  
    // inline은 box가 아니고 가로로 배열되는 텍스트같은 녀석이다. width, height와 쓸 수 없다  
}  
  
.box:nth-child(3) {    // 세번째 사각형만 이런식으로 조작할 수 있다  
    margin-left: 20px;  
}  
  
하지만 Flex Box에서는 자식을 이용하지 않는다.  
Flexbox Container를 이용해서 모든걸 한다.  
  
<body>  
    <div class="box"></div>  
    <div class="box"></div>  
    <div class="box"></div>  
</body>  
  
body {  
    display: flex;    // 플렉스  
}  
  
.box {  
    backgrouhd: blue;  
    width: 100px;  
    height: 100px;  
}  
  
box에 디스플레이를 설정하지 않고 부모인 body를 조작했다. body는 flex container이다.  
=> 부모가 자식의 위치를 조절할 수 있다는 말이다.  
  
flex는 가로, 세로 방향으로 위치를 바꿀 수 있는데,  
main axis는 가로이다. (row)  
  
cross-axis는 vertical 세로이다. 용어를 알아두자.  
(flex direction이 row일때 이야기이다. 반대일 경우 서로 바뀐다. 기본방향은 row)  
  
main axis 방향으로 아이템을 옮기기위해 justify-content를 사용한다.  
cross axis 방향으로 아이템을 옮길때는 align-items를 사용한다.  
body {  
    flex-direction: row;    // 기본이 가로라 안적어도 똑같다. 세로일때 바꾸면 됨.  
    display: flex;    // 플렉스  
    justify-content: center;    // 가운데정렬(가로방향이 DEFAULT)  
    justify-content: space-around; // 가로로 균등하게 사이를 두고 배열  
    align-item: center;  
    align-item: stratch;    // 길이가 닿는데까지 늘리기(height가 없어야 동작한다)  
}  
  
child:nth-child(2) {  
    align-self: center;  
}  
  
거의 모든경우 부모에 의해 자식의 위치가 결정되지만, 예외적인게 두개있는데  
위처럼 align self로 위치를 변경할 수 있다.  
align이라는 이름처럼 cross-axis 방향으로 움직인다.  
  
child:nth-child(2) {  
    order: 1;  
}  
  
또 하나는 오더조절이다. 위와같이 할 경우,  
기본 order는 0인데 두번째 자식의 경우 1이 되어서 우선순위가 뒤로 밀린다.  
1,2,3이 있었으면 1, 3 ,2 가 되는 것이다.  
=> HTML이 바뀌는 것은 아니다.  
  
Flex Box는 같은 라인에 있도록 배열하는데만 신경쓰기 때문에,  
width를 설정해도 상황에따라 적용되지 않을 수 있다.  
(예를들어 가로로 7개를 배치하면 200px짜리 7개라 넘칠때 200보다 적게 구겨서 넣어진다)  
.father {  
    display: flex;  
    // flex-wrap: nowrap;     // 기본값. 그대로 구겨서 넣음  
    flex-wrap: wrap;     // 자식들의 width를 키져줌. 줄이 넘어가더라도  
}  
  
하지만 위처럼 설정할 수 있다.  
  
위처럼 wrap일때 줄이 넘어갈 수 있는데,  
넘어갈때 줄 간의 여백간격은 아래처럼 설정할 수 있다.  
.father {  
    display: flex;  
    flex-wrap: wrap;     // 자식들의 width를 키져줌. 줄이 넘어가더라도  
    align-content: flex-start;    // 줄이 넘어갈때 여백없이 딱붙어서  
}  
  
  
flex-shrink  
.father {  
    display: flex;  
    flex-wrap: no-warp; // 짜부될 수 있음  
}  
  
.child:nth-child(2) {  
    // flex-shrink: 1;  // 균등하게 짜부됨  
    flex-shrink: 2;  // 얘만 두배로 짜부됨  
}  
  
  
flex-grow  
.father {  
    display: flex;  
    flex-wrap: no-warp; // 짜부될 수 있음  
}  
  
.child:nth-child(2) {  
    // flex-grow: 0;  // 창이 늘어나도 width를 지키며 서로 사이에 간격이 있음  
    flex-grow: 1;  // 늘어나는만큼 얘만 늘어나서 옆에 애들과 붙음  
}  
  
=> 한자식이 glow 2 , glow 1이면 그만큼 비율로 늘어난다.  
이것들은 반응형 디자인을 할때 좋고, 모바일에서도 활용하기가 좋다.  
  
.father {  
    display: flex;  
    flex-direction: row-reverse;  
}  
  
reverse를 하면 1,2,3,4로 배치된 애들이 HTML 수정없이 4,3,2,1로 배치된다.  
   
