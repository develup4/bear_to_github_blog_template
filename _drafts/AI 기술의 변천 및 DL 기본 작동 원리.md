# AI 기술의 변천 및 DL 기본 작동 원리
### 2021-06-24
#machine_learning

**< AI 기술의 변천 >**
 
**1. Rule based system (1950년대 ~)**
인간이 정립한 논리와 규칙에 따라 기계가 판단
: 개는 털이 있다 꼬리가 있다 짖는다
 
=> 수많은 if문
 
**2. Machine Learning(1980년대 ~)**
전문가들이 정교하게 모델링한 규칙들을 기계가 학습
학습은 하지만 규칙은 전문가의 Threshold에 의존(경험적 요소)
 
![](AI%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EB%B3%80%EC%B2%9C%20%EB%B0%8F%20DL%20%EA%B8%B0%EB%B3%B8%20%EC%9E%91%EB%8F%99%20%EC%9B%90%EB%A6%AC/image.png)
**3. Deep Learning(2010년대~)**
규칙도 학습하여 사전적 정보 없이도 기계가 데이터 학습 가능
 
1번 ) 2번 ) 3번 포함관계
 
**< 머신러닝의 유형 >**
- Supervised Learning : 레이블(정답)이 있는 데이터로 학습
![](AI%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EB%B3%80%EC%B2%9C%20%EB%B0%8F%20DL%20%EA%B8%B0%EB%B3%B8%20%EC%9E%91%EB%8F%99%20%EC%9B%90%EB%A6%AC/image%202.png)
- Unsupervised Learning : 정답없이 학습하여 공통구조나 특징을 예측 - 클러스터링
![](AI%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EB%B3%80%EC%B2%9C%20%EB%B0%8F%20DL%20%EA%B8%B0%EB%B3%B8%20%EC%9E%91%EB%8F%99%20%EC%9B%90%EB%A6%AC/image%203.png)
- Reinforcement Learning - 보상시스템으로 학습
 
< 딥러닝의 발전 >
알고리즘 향상 / 빅데이터 발달 / GPU등 컴퓨팅파워 발달 및 클라우드 연결 / 오픈소스 프레임워크 지원
 
< 기본 용어 >
타깃(target) : 기대 출력을 의미한다.
매핑(mapping) : 입력과 타깃의 관계로 입력을 representation로 변환, 연관시키는 것을 의미한다. 
가중치(weight) : 머신 러닝, 딥러닝 모두 결국은 가장 효율적인 식 을 찾는 것이 목표이며, 이런 식 또는 식에 필요한 파라미터를 말한다.
손실함수(loss function) : 타깃과 출력 값의 차이를 계산하는 함수 
역전파(Backpropagation) : 손실함수의 결과를 개선하기 위해서 다시 결과에서부터 가중치를 수정하는 과정이다. 이를 옵티마이저 (optimizer)가 담당한다. 
 
< 딥러닝 기본 작동 원리 >
인간의 신경세포과 같은 구조로 동작한다고 한다.
![](AI%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EB%B3%80%EC%B2%9C%20%EB%B0%8F%20DL%20%EA%B8%B0%EB%B3%B8%20%EC%9E%91%EB%8F%99%20%EC%9B%90%EB%A6%AC/image%204.png)
![](AI%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EB%B3%80%EC%B2%9C%20%EB%B0%8F%20DL%20%EA%B8%B0%EB%B3%B8%20%EC%9E%91%EB%8F%99%20%EC%9B%90%EB%A6%AC/image%205.png)
1. 데이터를 입력한다.
2. 여러 레이어를 통해 예상 결과값을 만든다. (매핑)
3. 실제 값과 비교해서 그 차이를 구한다. (타겟과 손실함수)
4. 차이를 줄이기 위한 방법으로 앞의 충돌의 가중치를 수정해준다. (역전파)
5. 이 방법의 반복으로 규칙을 계속 개선한다.
![](AI%20%EA%B8%B0%EC%88%A0%EC%9D%98%20%EB%B3%80%EC%B2%9C%20%EB%B0%8F%20DL%20%EA%B8%B0%EB%B3%B8%20%EC%9E%91%EB%8F%99%20%EC%9B%90%EB%A6%AC/image%206.png)
