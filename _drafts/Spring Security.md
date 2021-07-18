# Spring Security
#spring #security

pom.xml
```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

이렇게 추가만 해줘도,
스프링을 실행해보면 로그에

`using generated security password: 02924524-cc99-47fe-9e1a-7fbe9f5031a4`
아래와같은 패스워드가 나오고

그동안 잘되던 rest-api도 401 auth가 뜬다.

헤더에 authorization에서 basic auth를 선택해서 user:user, password:위에 값을 하면 값이 나오고 200 ok가 나온다.


이제 사용자 지정 계정을 쓰려면 아래와 같이 추가를 하면 지정된 계정으로 쓸수있

resoures/application.yml
```java
spring:
  jpa:
    show-sql: true
  messages:
    basename: messages
  security:
    user:
      name: username
      password: passw0rd
```


설정파일외에 코드로도 아래처럼 추가가 가능하다

```java
package com.example.restfulwebservice.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests().antMatchers("/h2-console/**").permitAll();
        http.csrf().disable();
        http.headers().frameOptions().disable();
    }

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth)
        throws Exception {
        auth.inMemoryAuthentication()
                .withUser("kenneth")
                .password("{noop}test1234")
                .roles("USER");
    }
}
```