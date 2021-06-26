---
title:  CSS Layout - Grid

categories: CSS 
tags: Grid  layout
 
---

  
.father {  
    display: grid;  
    grid-template-columns: 20px 55px 89px 100px; // column이 몇 개인지 간격은 어떤지 설정  
    grid-template-rows: 100px 50px 300px; // 이번엔 row  
    column-gap: 10px;    // 열간 간격  
    row-gap: 10px;    // 행간 간격  
    gap: 10px;    // 위 두줄과 같다  
}  
  
  
Grid도 Flex Box처럼 부모에 display를 설정해서 적용한다.  
  
<div class="grid">  
    <div class="header"></div>  
    <div class="content"></div>  
    <div class="nav"></div>  
    <div class="footer"></div>  
</div>  
  
.grid {  
  display: grid;  
  grid-template-columns: auto 200px; // 가능한만큼 크게 200px까지  
  grid-template-rows: 100px repeat(2, 200px) 100px; // == 100px 200px 200px 100px  
  grid-template-areas:  
    "header header header header"  
    "content content content nav"  
    "content content content nav"  
    "footer footer footer footer";  
}  
  
.header {  
  background-color: #2ecc71;  
  grid-area: header; // grid가 이것을 이해하려면 반드시 필요하다!  
}  
  
.content {  
  background-color: #3498db;  
  grid-area: content;  
}  
  
.nav {  
  background-color: #8e44ad;  
  grid-area: nav;  
}  
  
.footer {  
  background-color: #f39c12;  
  grid-area: footer;  
}  
  
grid-template-areas에 집중해서 봐보자  
그리고 grid-area에 이름을 써줘야 인식할 수 있음을 반드시 주의해야 한다.  
(classname은 grid에서는 소용이 없다)  
  
.grid {  
  display: grid;  
  gap: 10px;  
  grid-template-columns: repeat(4, 100px);  
  grid-template-rows: repeat(4, 100px);  
}  
  
.header {  
  background-color: #2ecc71;  
}  
  
.content {  
  background-color: #3498db;  
 grid-column-start: 1;  
  grid-column-end: 4;  
  grid-row-start: 2;  
  grid-row-end: 4;  
}  
.nav {  
  background-color: #8e44ad;  
  grid-row-start: 2;  
  grid-row-end: 4;  
}  
  
.footer {  
  background-color: #f39c12;  
  grid-column-start: 1;  
  grid-column-end: 5;  
}  
  
grid template없이 생짜로 짜면 위와 같다.  
  
grid-column-start: 1  
grid-column-end: 5의 의미가 중요한데,  
  
한칸에서 세로줄 하나가 기준이다.  
줄 5개까지의 영역이 해당 css로 적용될 것이다.  
  
근데 위 방법도 더 쉬운 방법이 있다.  
short cut이다  
grid-column: 1 / 5;  
grid-column: 1 / -1;  // -1은 마지막  
grid-column: 1 / -2;  // -2는 마지막 전꺼(역순으로 쭉감)  
  
근데 더 쉬운 방법도 있다.  
span이다  
grid-column: span 4    // line으로 세지않고 이건 칸이다  
  
네모칸 수로 세기때문에 더 쉬울 수 있다.  
근데 이건 시작점을 알수없으니 아래와 같이 할수도 있다.  
grid-column: 2 / span 2  
  
2부터 시작해서 두칸이다.  
  
선에 이름을 붙일 수도 있다.  
.grid {  
  display: grid;  
  gap: 10px;  
  grid-template-columns: [first-line] 100px [second-line] 100px [third-line] 100px [fourth-line] 100px [fifth-line];  
  grid-template-rows: repeat(4, 100px [sexy-line]);  
}  
  
.content {  
  background-color: #3498db;  
  // grid-column: 1 / -2;  
  // grid-row: span 2;  
  grid-column: first-line / fourth-line;  
  grid-row: sexy-line 1 / sexy-line 3;    // sexy line 중 첫번째 세번째  
}  
  
  
**1fraction(1fr)**  
repeat(4, 1fr)  
  
px처럼 단위이다. fraction은 사용가능한 공간을 의미한다.  
(그리드 안에서 사용가능한 공간을 의미한다. 따라서 공간이 없으면 안나오니 주의)  
  
그리드에서는 fr 단위를 쓰는게 좋다.  
모바일이나 피씨나 유연하게 사용이 가능하다. (비율로 생각하면된다)  
  
grid-template-rows: 4fr 1fr 1fr;  
  
이러면 처음 것이 2/3을 차지하게 된다.  
  
  
지금까지 점점 편하게 쓰는 방향으로 가고있지만 그중 최고는…  
처음에 다룬 grid template이다. 굿굿!  
.grid {  
  display: grid;  
  gap: 5px;  
  height: 50vh;  
  grid-template:  
    "header header header header" 1fr    // 높이를 지정할 수 있다  
    "content content content nav" 2fr  
    "footer footer footer footer" 1fr / 1fr 1fr 1fr 1fr;    // 슬러쉬 뒤에는 가로의 길이를 지정해주면 된다(repeat 안됨)  
}  
  
길이가 지정가능하다. 그리고 fr로해서 창크기가 변해도 비율이 유지된다.  
  
모든 그리드는 자식을 가지고 있고, 자식을 늘려서 본인을 채우게 한다.  
그래서 grid칸을 어떻게 채울지는 justify-items: stretch가 기본이다.  
(세로는 align-items, 둘 다 하려면 place-items: stretch / center)  
  
  
grid에서도 flex처럼 justify-content, align-content를 쓸 수 있다  
place-content는 가로, 세로 둘다가능하다.  
place-content: end center;  
  
다만 전체 그리드가 움직이는거라는걸 주의하자.  
  
각각 그리드 한칸에 대해서 배치를 주려면 justify-self, align-self를 쓴다.  
마찬가지로 place-self로 둘다 가능하다.  
  
이제 마지막으로 그리드는 16칸인데 아이템이 25개면 어떨까?  
아이템들을 서버에서 받아오는거라면 몇 개가 될지 예측하지 못할수도 있다.  
이럴때는 grid auto를 쓰자.  
.grid {  
  color: white;  
  display: grid;  
  gap: 5px;  
  grid-template-columns: repeat(4, 100px);  
  // grid-template-rows: repeat(4, 100px);  
  grid-auto-rows: 100px;     // 100 크기로 계속 생겨남  
}  
  
  
column의 경우는 아래와 같이,  
.grid {  
  color: white;  
  display: grid;  
  gap: 5px;  
  grid-template-columns: repeat(4, 100px);  
  grid-template-rows: repeat(4, 100px);  
  grid-auto-flow: column;     //  
  grid-auto-columns: 100px;     //  
}  
  
  
세로는 고려해야 할점이…  
그리드칸 수보다 요소가 많을때, 디폴트는 행이 늘어는데,  
grid-auto-flow로 열이 늘어나도록 먼저 설정을 해야한다.  
  
이 경우 배열도 아래와 같다.  
1 5  
2 6  
3 7  
4 8 …  
  
minmax로 창크기와 상관없이 최소크기 최대크기를 지정할 수 있다.  
grid-template-columns: repeat(5, minmax(100px, 1fr));  
  
  
반응형 웹을 만드는데 중요한 auto-fill과 auto-fit이다.  
auto-fill은 한줄에 들어갈 수 있는만큼 채우는 것이다.  
  
|ㅁㅁㅁㅁㅁ| 였으면 |ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ| 창이 늘어나면 더 요소가 들어가는것이다.  
auto-fit은 늘어난 크기에 맞춰 요소가 늘어나는 것이다.  
.grid:first-child {  
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));  
}  
  
.grid:last-child {  
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));  
}  
  
min-content, max-content는 div안에 글자라던지 컨텐츠가 있을때,  
그것에 맞게 늘어나던지 div에 꽉차도록 최소한으로 줄이는 역할을 한다.  
  grid-template-columns: min-content max-content;  
  
  
일반적인 경우에 이정도가 적당하다.  
  grid-template-columns: repeat(auto-fill, minmax(max-content, 1fr));  
  
   
