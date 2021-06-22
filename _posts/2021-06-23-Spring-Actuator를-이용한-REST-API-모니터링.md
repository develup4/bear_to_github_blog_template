---
title:  Spring Actuator를 이용한 REST API 모니터링

categories: Spring 
tags: Actuator  REST-API  monitoring
 
classes: wide
---

  
`application.yml`  
management:  
  endpoints:  
    web:  
      exposure:  
        include: "*"  
  
위같이 설정만 추가한뒤 아래 url 접속하면  
localhost:8080/actuator  
  
제이슨정보뜬다  
잘가공해서 쓰면된다  
  
  
  
  
  
<dependency>  
    <groupId>org.springframework.data</groupId>  
    <artifactId>spring-data-rest-hal-browser</artifactId>  
</dependency>  
  
이건 다른건데  
이걸 하면 더 자세하게 나온다  
