---
title:  DEVIEW 2020 GraphQL 세션

categories: backend 
tags: deview2020  graphql
 
---

  
**- GraphQL 구조와 보안**  
   
GraphQL 쿼리가 노출되면 마이크로서비스 구조가 그대로 드러나 보안에 취약할 수 있다.  
Deview 2020에서 본 내용인데,  
GraphQL gateway를 둬서 그곳으로 쿼리에 대한 해시를 전달하고,  
gateway에서는 해시에 매치된 쿼리를 사용하는 방식을 사용하여 보안성을 지켰다.  
  
![]({{ site.url }}{{ site.baseurl }}/assets/images/2021-07-19-DEVIEW 2020 GraphQL 세션/dthumb-phinf.pstatic.net.png)  
  [GraphQL이 가져온 에어비앤비 프론트앤드 기술의 변천사](https://tv.naver.com/v/16970011)   
   [NAVER Engineering | 박호준 - GraphQL이 가져온 에어비앤비 프론트앤드 기술의 변천사(부제: REST환경에서 GraphQL 기반 UI 설계하기)](https://tv.naver.com/v/16970011)   
  [tv.naver.com](https://tv.naver.com/v/16970011)    
Ps. fragment를 굉장히 많이 사용하더라. 그리고 GraphQL도 스펙일 뿐이라는걸 알게되었다.  
   
 https://deview.kr/data/deview/session/attach/1100_T1_%E1%84%87%E1%85%A1%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%92%E1%85%A7%E1%86%AB_GraphQL%20API%20%E1%84%81%E1%85%A1%E1%84%8C%E1%85%B5%E1%86%BA%E1%84%80%E1%85%A5%20%E1%84%8B%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A2%E1%84%87%E1%85%A9%E1%84%8C%E1%85%B5%20%E1%84%86%E1%85%AF.pdf  
**- GraphQL과 엔드포인트**  
   
/Post  
/User  
/Image  
와 같은 것을 엔드 포인트라고 부른다.  
   
GraphQL은 관계를 가지고 한번에 가져올 수 있으니(Under-fetch 문제),  
엔드포인트가 하나이며 오케스트레이션에 유리하다.  
   
그리고 APM(api 모니터링 환경)이 필수이며,  
유료이긴 하지만 Apollo에 그러한 환경이 있다.  
   
   
**- Principled GraphQL과 버저닝**  
   
Schema는 점진적으로 구축되어야 하고, 원활하게 발전되어야 한다.  
Schema에 내용이 추가/제거되어도 기존 api를 활용할 수 있기 때문에 원칙적으로 버저닝이 필요없다.  
가끔 REST api를 보면 api/v2 이런 형식을 자주 볼 수 있는데 이것이 버저닝의 흔적이다.  
(하위 호환이 안되므로 기존 api를 유지한다)  
   
쿼리 변경시에는 breaking change에 대한 정책이 필요하다.  
(not null이 nullable로 바뀌는 경우는 가능. forced로 해결을 할지?)  
   
Apollo studio를 통하여, CLI를 통해 validation check를 할 수 있으며,  
breaking change가 있는지 원인은 무엇인지 알려준다.  
(prisma에서 generate할때와 비슷하다)  
   
   
**- GraphQL과 data fatigue**  
  
REST api는 모든 데이터를 다 주므로(더군다나 상용이라면 엄청난), 사용을 위해서는 데이터를 분석해야 한다.  
이는 굉장히 피로한 작업이며, GraphQL에서는 요청하는 데이터만을 받으므로 장점이 있다.  
   
   
**- annotation을 이용한 GraphQL 분기처리**  
mobileBooking @skip(if: $isPC)  
pcBooking @include(if: $isPC)  
  
