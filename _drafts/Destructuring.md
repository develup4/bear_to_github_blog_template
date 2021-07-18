# Destructuring
## ECMA Script 6(TODO)
#language #javascript #es6

 
const settings = {
  color: {
    theme: "dark"
  }
};

const { color: { theme, valid = true } = {} } = settings;
console.log(color);


자바스크립트 객체를 꺼낼때 .(dot) 연산자를 통해 접근하는게 귀찮아서,
따로 변수에 넣어서 변수를 조작했는데, 이제 한줄로 풀어서 쓰는게 가능하다.
valid = true 처럼 default value를 쓸수도 있어서 만약 객체에 값이 없더라도 undefined를 피할 수 있다.
마지막 console.log에서 원래는 최종 destructuring의 결과물만 쓸수 있기때문에 중간인 color는 값이 없어야하지만
이것도 default값인 ={}에 의해 빈객체 값을 가지게 된다.

const days = ["Mon", "Tue, "Wed"];
cosnt [mon, tue, wed, sun = "Sun"] = days;

console.log(mon, sun);

별로 쓸일은 없다는 array destructuring이다.
이경우도 디폴트 밸류가 가능하다.

**Renaming with destructuring**
const settings = {
  color: {
    chosen_color: "dark"
  }
};

const {
  color: { chosen_color: chosenColor = "light" }
} = settings;

console.log(chosenColor);

저렇게 컨벤션에 안맞는 변수같은걸 받는다치면 저런식으로 이름을 고치고 디폴트값을 쓸수도 있다.


const saveSettings = ({follow, alert, color = “blue”}) => {};

saveSettings({
  follow: true,
  alert: true,
  mkt: false
});

파라메터도 디스트럭쳐링 가능. 디폴트값 가능


- Value Shorthands
{alert: alert} 과 같이 이름이 같은 키와 값은 하나로 줄여서 쓸 수 있다. {alert}

// swapping by array destructuring

let mon = “sat”;
let sat = “mon”;

[sat, mon] = [mon, sat];


// skipping technicque

const numbers = [“1”, “2”, “3”, “4”];

const [ , , rd, th] = numbers;

console.log(rd, th);


 