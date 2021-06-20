# Python
python naming convention => snake case(_)

list 수정가능한 리스트
days = [“mon”, “tue”, “wed”, 4, True]

배열이 아니다
여러타입 가능

아래와 같은 표현 가능
days[3]
len(days)
“mon” in days
min(days)
int(days[4]) 일종의형변환

Tuple(수정불가능한 리스트)
days=(“mon”, “tue”, “wed”)

기능은동일하지만 수정불가능

dictionary
nico = {
  “name” : “nico”,
  “age”: 29
}

nico[“name”] = “coco”

따옴표 주의


>> function args는기본적으로 순서에 의존하지만 keyworded argument로 쓸수도 있다.

def plus(a,b):
  return a+b

plus(b=3, a=1)



조건문
elif a is not 10 and b is 5:


반복문
for potato in days:


module
from math import ceil, fsum as sexysum
전부 import하지말고 필요한거만 하자

전부 =>
import math