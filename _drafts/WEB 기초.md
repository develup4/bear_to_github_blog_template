# WEB 기초
### 2021-07-11
#backend #web
팀 버나스리가 웹을 창안해 내고 전 세계의 문서가 웹으로 올라왔다.
(웹 20주년 기념행사에서 직접 뵀다 ㅎㅎ)
 
![](WEB%20%EA%B8%B0%EC%B4%88/dthumb-phinf.pstatic.net.jpg)
  [The next web](https://www.ted.com/talks/tim_berners_lee_the_next_web?utm_campaign=tedspread&utm_medium=referral&utm_source=tedcomshare) 
   [20 years ago, Tim Berners-Lee invented the World Wide Web. For his next project, he’s building a web for open, linked data that could do for numbers what the Web did for words, pictures, video: unlock our data and reframe the way we use it together.](https://www.ted.com/talks/tim_berners_lee_the_next_web?utm_campaign=tedspread&utm_medium=referral&utm_source=tedcomshare) 
  [www.ted.com](https://www.ted.com/talks/tim_berners_lee_the_next_web?utm_campaign=tedspread&utm_medium=referral&utm_source=tedcomshare) (위 TED에서 이제는 데이터를 위한 인터넷을 주장하고 있다)
 
WWW는 다음의 세 가지 요소로부터 시작된다.
### - URI : 데이터는 어디에 있는가?

### - HTTP : 데이터는 어떻게 손에 넣는가?

### - HTML : 데이터는 어떻게 표현하는가?

 
이 세 가지는 지금도 변하지 않았다.
http://blog.livedoor.jp/dankogai/search?q=WEB%2BDB를 예로 들면
 
http://
=> 어떤 방법(Scheme)으로 데이터를 가지러 갈 것인가?
 
blog.livedoor.jp
=> 서버(host)는 어떤 것인가?
 
/dankogai/search
=> 서버 내의 위치(path)는 어디인가?
(파일명이 생략되어 있다. 웹 서버 설정마다 다르지만 기본 파일인 index.html, default.htm을 부른다)
 
?q=WEB%2BDB
 => 질의(query)는 무엇인가?
 
이것으로도 충분히 획기적이었으나,
단순 문서의 열람을 넘어 웹 어플리케이션에 대한 사람들의 욕망에 의해
새로운 기술들이 태동했다.
 
먼저 **CGI(common gateway interface)**이다.
간단히 설명하면 웹 서버가 정적인 html을 던져주고 끝이 아니라 html을 생성해서 던져줄 수 있게 된 것이다.
펄(Perl)을 통해 주로 개발되었으며, 이를 통해 전자 상거래 등 웹서비스가 시작되게 되었다.
(웹 언어는 P로 시작하는 것이 많다. Perl, Php, Python, …)
 
이후 자바 서블릿이 대세 기술이 되어, 강력한 자바를 통해 웹 서버를 만들 수 있게 되었다.
자바 코드 내에서 html을 생성하여 response로 보낼 수 있게 된 것이다.
(out.println(“<p>contentscontents</p>”;)
 
하지만 코드 내에서 마크업을 생성해내다보니 디자이너와의 협업이 어려웠고,
JSP가 대세로 떠오른다. 아이디어는 정반대였다.
서블릿은 자바에 HTML을 넣었고, JSP는 반대로 HTML에 자바 코드를 넣었다.
(<% price += 1000 %>)
 
Php 역시 HTML 내에 코드를 심는 방식이다.
<? php
    $arg1 = $_GET[‘arg1’;
    $arg2 = $_GET[‘arg2’;
    $result = $arg1 + $arg2;
    echo htmlspecialchars($result);
?>
(Php 코드는 몰라도 어디선가 본적이 있는 듯 하다. 익숙하다)
 
 
**- 리소스를 취득하는 과정**
http에서는 한번의 요청에 한 리소스 밖에 취득하지 못한다.
따라서 예를 들어 이미지가 많이 들어있는 페이지에서는 이미지 수만큼의 http 요청이 발생한다.
웹 브라우저가 html을 먼저 해석해서 img 태그를 확인하고 src 속성의 url을 통해 이미지를 다시 취득하는 것이다.
 
TCP/IP는 브라우저 등으로부터 받은 http 요청 등의 정보를 패킷이라는 단위로 분할하여 송신하고,
받은쪽에서는 그것을 조립하여 웹 서버 등의 어플리케이션으로 넘긴다.
 
참고로 URN은 유니크한 이름으로 위치가 바껴도 그 자체로 유니크한 개념인데, 실제로는 안쓰이기 때문에 URL, URN을 포함하는 개념인 URI는 사실상 URL과 같은 개념이 되었다.
 
**- GET / POST 방식에 대해 (?q=arg1=123&arg2=456)**
물음표를 쿼리 문자열이라하며 q를 매개변수라고 한다. 매개변수가 여러개일때는 &로 연결한다
POST 방식도 위 형식은 동일하며, 메시지의 본문에 들어간다는 차이가 있다
GET 방식은 매개변수를 포함하고 있어, URL 자체가 상태를 가지고 있다. 검색 결과를 즐겨찾기로 등록하는 등의 일이 가능하다
브라우저에 따라 한글 url을 지원하지 않을때, 퍼센트 인코딩이 된다. 가끔보는 이상한 uri가 이것이다.
(홍 ED998D 길 EAB8B8 동 EB8F99 => %ED%99%8D%EA%B8%B8%EB%8F%99)

