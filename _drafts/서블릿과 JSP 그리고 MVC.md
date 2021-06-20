# 서블릿과 JSP 그리고 MVC
앞서 서블릿의 개념과 API들을 살펴보았다. 이를 통해 회원관리 웹 어플리케이션을 만들어보고 한계도 느껴보고 JSP를 도입해보자.

모델과 repository를 생성하는 부분은 뻔해서 생략하였다. 바로 서블릿 작성으로 가보자.

```java
@WebServlet(name = "memberFormServlet", urlPatterns = "/servlet/members/new-
  form")
  public class MemberFormServlet extends HttpServlet {
      private MemberRepository memberRepository = MemberRepository.getInstance();
@Override
      protected void service(HttpServletRequest request, HttpServletResponse
  response)
              throws ServletException, IOException {
          response.setContentType("text/html");
          response.setCharacterEncoding("utf-8");

PrintWriter w = response.getWriter();
          w.write("<!DOCTYPE html>\n" +
                  "<html>\n" +
                  "<head>\n" +
                  "    <meta charset=\"UTF-8\">\n" +
"    <title>Title</title>\n" +
"</head>\n" +
"<body>\n" +
"<form action=\"/servlet/members/save\" method=\"post\">\n" +
"    username: <input type=\"text\" name=\"username\" />\n" +
"    age:      <input type=\"text\" name=\"age\" />\n" +
" <button type=\"submit\">전송</button>\n" + "</form>\n" +
"</body>\n" +
"</html>\n");
}
}
```

아이고야...HTML을 직접 생성해서 response로 전달하고 있다. 뭐...어쨌건 일단 form을 전달했으니 form에서 전달되는 post 메시지를 처리할 수 있는 서블릿을 또 만들어보자.

```java
@WebServlet(name = "memberSaveServlet", urlPatterns = "/servlet/members/save")
public class MemberSaveServlet extends HttpServlet {
    private MemberRepository memberRepository = MemberRepository.getInstance();
@Override
    protected void service(HttpServletRequest request, HttpServletResponse
response)
            throws ServletException, IOException {
        System.out.println("MemberSaveServlet.service");
        String username = request.getParameter("username");
        int age = Integer.parseInt(request.getParameter("age"));
        Member member = new Member(username, age);
        System.out.println("member = " + member);
        memberRepository.save(member);
        response.setContentType("text/html");

response.setCharacterEncoding("utf-8");
        PrintWriter w = response.getWriter();
        w.write("<html>\n" +
"<head>\n" +
" <meta charset=\"UTF-8\">\n" + "</head>\n" +
"<body>\n" +
"성공\n" +
"<ul>\n" +
                "    <li>id="+member.getId()+"</li>\n" +
                "    <li>username="+member.getUsername()+"</li>\n" +
" <li>age="+member.getAge()+"</li>\n" + "</ul>\n" +
"<a href=\"/index.html\">메인</a>\n" +
“</body>\n" +
"</html>");
}
}
```

MemberSaveServlet 은 다음 순서로 동작한다.
1. 파라미터를 조회해서 Member 객체를 만든다.
2. Member 객체를 MemberRepository를 통해서 저장한다.
3. Member 객체를 사용해서 결과 화면용 HTML을 동적으로 만들어서 응답한다.





템플릿 엔진으로
지금까지 서블릿과 자바 코드만으로 HTML을 만들어보았다. 서블릿 덕분에 동적으로 원하는 HTML을 마음껏 만들 수 있다. 정적인 HTML 문서라면 화면이 계속 달라지는 회원의 저장 결과라던가, 회원 목록 같은 동적인 HTML을 만드는 일은 불가능 할 것이다.
그런데, 코드에서 보듯이 이것은 매우 복잡하고 비효율 적이다. 자바 코드로 HTML을 만들어 내는 것 보다 차라리 HTML 문서에 동적으로 변경해야 하는 부분만 자바 코드를 넣을 수 있다면 더 편리할 것이다. 이것이 바로 템플릿 엔진이 나온 이유이다. 템플릿 엔진을 사용하면 HTML 문서에서 필요한 곳만 코드를 적용해서 동적으로 변경할 수 있다.
템플릿 엔진에는 JSP, Thymeleaf, Freemarker, Velocity등이 있다.



자 그러면 JSP를 사용해보자. 옛날에 서블릿, JSP같은책들 많이도 나왔는데 구분도 못했는데 이제는 알수있따.

```java
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
  <html>
  <head>
      <title>Title</title>
  </head>
<body>
<form action="/jsp/members/save.jsp" method="post"> username: <input type="text" name="username" /> age: <input type="text" name="age" /> <button type="submit">전송</button>
</form>
  </body>
  </html>
```

<%@ page contentType="text/html;charset=UTF-8" language="java" %>
첫 줄은 JSP문서라는 뜻이다. JSP 문서는 이렇게 시작해야 한다.


다른 템플릿엔진(django template, pug 같은것도 봤으니 뭔지 대충 알것이다.

회원 등록 폼 JSP를 보면 첫 줄을 제외하고는 완전히 HTML와 똑같다. JSP는 서버 내부에서 서블릿으로
변환되는데, 우리가 만들었던 MemberFormServlet과 거의 비슷한 모습으로 변환된다.

실행
http://localhost:8080/jsp/members/new-form.jsp
실행시 .jsp 까지 함께 적어주어야 한다.


> 즉, 단순 html을 반환하는 서블릿이라면 서블릿을 작성할 필요없이 jsp만 작성하면 그 url롲접속시 동일한 처리가 가능하다는 이야기이다.  


이번엔 회원저장을 jsp로 구현해보자. 아까보다 매운맛이다.

```java
<%@ page import="hello.servlet.domain.member.MemberRepository" %>
  <%@ page import="hello.servlet.domain.member.Member" %>
  <%@ page contentType="text/html;charset=UTF-8" language="java" %>
  <%
   //
request, response 사용 가능
MemberRepository memberRepository = MemberRepository.getInstance();
System.out.println("save.jsp");
String username = request.getParameter("username");
int age = Integer.parseInt(request.getParameter("age"));
Member member = new Member(username, age);
System.out.println("member = " + member);
memberRepository.save(member);
%>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
성공
  <ul>
      <li>id=<%=member.getId()%></li>
      <li>username=<%=member.getUsername()%></li>
      <li>age=<%=member.getAge()%></li>
</ul>
<a href="/index.html">메인</a>
  </body>
  </html>
```

보면 자바코드가 기냥 들어가 있다.

회원 저장 JSP를 보면, 회원 저장 서블릿 코드와 같다. 다른 점이 있다면, HTML을 중심으로 하고, 자바
코드를 부분부분 입력해주었다. <% ~ %> 를 사용해서 HTML 중간에 자바 코드를 출력하고 있다.



> 자바진영의 원대한 꿈. 자바는 자바 가상머신 위에서 동작한다. 그래서 웹 브라우저에 가상머신을 탑재해서 서버와 클라이언트간에 자바 바이트 코드를 전송해서 웹 어플리케이션을 구현하고 싶은 원대한 목표가 있었는데, 결국 자바스크립트가 동일한 방식으로 웹 세계를 지배해버리고 말았다.  



서블릿과 JSP의 한계
서블릿으로 개발할 때는 뷰(View)화면을 위한 HTML을 만드는 작업이 자바 코드에 섞여서 지저분하고 복잡했다.
JSP를 사용한 덕분에 뷰를 생성하는 HTML 작업을 깔끔하게 가져가고, 중간중간 동적으로 변경이 필요한 부분에만 자바 코드를 적용했다. 그런데 이렇게 해도 해결되지 않는 몇가지 고민이 남는다.
회원 저장 JSP를 보자. 코드의 상위 절반은 회원을 저장하기 위한 비즈니스 로직이고, 나머지 하위 절반만 결과를 HTML로 보여주기 위한 뷰 영역이다. 회원 목록의 경우에도 마찬가지다.



코드를 잘 보면, JAVA 코드, 데이터를 조회하는 리포지토리 등등 다양한 코드가 모두 JSP에 노출되어 있다. JSP가 너무 많은 역할을 한다. 이렇게 작은 프로젝트도 벌써 머리가 아파오는데, 수백 수천줄이 넘어가는 JSP를 떠올려보면 정말 지옥과 같을 것이다. (유지보수 지옥 썰)
MVC 패턴의 등장
비즈니스 로직은 서블릿 처럼 다른곳에서 처리하고, JSP는 목적에 맞게 HTML로 화면(View)을 그리는 일에 집중하도록 하자. 과거 개발자들도 모두 비슷한 고민이 있었고, 그래서 MVC 패턴이 등장했다. 우리도 직접 MVC 패턴을 적용해서 프로젝트를 리팩터링 해보자.



55페이지 mvc부터