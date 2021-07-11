---
title:  Golang syntax

categories: language 
tags: golang  syntax
 
---

  
  
   
package main    // 이 파일이 main 패키지에 포함된다는 뜻이다  
  
import "fmt"    // built in 패키지를 import하여 사용한다  
  
func main() {  
    fmt.Println("Hello world!")  
}   
  
main 함수가 없어도 라이브러리 개념으로 다른곳에서 사용할 수 있지만,  
그런 경우 단독으로 컴파일은 되지 않는다.  
  
package something  
  
import "fmt"  
  
func SayHello() {  
	fmt.Println("Hello")  
}  
  
별도의 파일에 something 패키지에 포함될 내용을 작성해보았다.  
여기서 접근지정자 개념이 나오는데,  
  
sayHello => private  
SayHello => public export  
  
대소문자에 의해 export 여부를 결정한다.  
언뜻보면 이상하지만 컨벤션을 겸하는 문법이라 좋은거 같기도 하다.  
  
type Account struct {  
	owner   string  
	Balance int  
}  
  
나중에 나올거지만 스트럭쳐에서도 멤버의 가시성을 첫문자의 대소문자로 구분할 수 있다.  
위 경우 Balance만 밖에서 접근할 수 있다.  
  
package main  
  
import "fmt"  
  
func main() {  
	name := "nico"  
	name = "lynn"  
	fmt.Println(name)  
}  
  
:=는 무척 이상하게 생겼지만 암시적으로 타입을 결정할 수 있는 연산자이다(implicit type determine)  
이 문법을 사용하면 변수를 추정하여 타입없이 바로 선언과 초기화를 할 수 있으며,  
함수안에서만 선언가능하고 전역적으로는 선언할 수 없다.  
  
package main  
  
import (  
	"fmt"  
	"strings"  
)  
  
func lenAndUpper(name string) (int, string) {    // 뒤에 괄호에 리턴형을 지정하고 멀티 리턴이 가능하다!  
	return len(name), strings.ToUpper(name)  
}  
  
func repeatMe(words ...string) {    // ...으로 가변 인자가 가능하다  
	fmt.Println(words)  
}  
  
func main() {  
	totalLenght, _ := lenAndUpper("nico")  
	fmt.Println(totalLenght)  
}  
  
멀티 리턴과 다중인자를 지원한다.  
전반적으로 정말 편하려고 만든거같다.  
  
func lenAndUpper(name string) (length int, uppercase string) {    // 리턴 변수를 바로 선언 가능  
	defer fmt.Println("I'm done")    // 함수가 끝난 뒤 코드가 실행되도록 한다  
	length = len(name)  
	uppercase = strings.ToUpper(name)  
	return  
}  
  
두번째 괄호안의 변수명 지정은 naked return 이라는 기능이다.  
리턴 변수를 바로 괄호에서 지정해서 함수내에서 따로 선언을 할 필요가 없다.  
  
그리고 defer 키워드는 뒤에 있는 문장을 함수가 끝난뒤에 실행하도록 해준다.  
  
	total := 0  
	for _, number := range numbers {  
		total += number  
	}  
  
  
- 반복문  
	if koreanAge := age + 2; koreanAge < 18 {  
		return false  
	}  
  
variable expression  
=> modern c++에 추가된 내용처럼 if 문안에서 변수를 선언할 수 있다.  
if 블록 안에서만 사용할 수 있으므로 더 숨길 수 있어 좋다.  
  
switch koreanAge := age + 2; koreanAge {  
	case 10:  
		return false  
	case 18:  
		return true  
    case koreanAge > 18:  
        return true;  
}  
  
switch에서도 variable expression을 사용할 수 있고, case에서 조건도 가능하므로  
if~else를 대체할 수 있다.  
  
func main() {  
	fmt.Println(canIDrink(18))  
	a := 2  
	b := &a  
	*b = 2020;  
	fmt.Println(a, *b)  
}  
  
포인터 개념과 연산자는 뭐 동일하다.  
  
import "fmt"  
  
func main() {  
	names := [5]string{"nico", "lynn", "dal"}   // 크기를 지정하면 Array  
  
	names := []string{"nico", "lynn", "dal"}    // 크기를 비워두면 Slice  
	names = append(names, "flynn")  
	fmt.Println(names)  
}  
  
golang의 태생을 고려할때, c언어에 익숙하면 아주 개념이 잘달라붙는다.  
array, slice로 구분되는것을 주의하고…  
append는 첫번째 인자로 슬라이스를 받는데…  
확깼다…역시 객체지향 개념이 전혀 없다.  
(하지만 뒤에서 반전)  
import "fmt"  
  
func main() {  
	nico := map[string]int{"name": 3, "age": 7}  
    value, exist := nico["name"]  
	for key, value := range nico {  
		fmt.Println(key, value)  
	}  
}  
  
map이고 for문 사용가능하다.  
exist도 받을 수 있다.  
  
삭제는 아래처럼 delete 함수로 한다.  
func (d Dictionary) Delete(word string) {  
	delete(d, word)  
}  
  
  
- Structure  
import "fmt"  
  
type person struct {  
	name    string  
	age     int  
	favFood []string  
}  
  
func main() {  
	favFood := []string{"kimchi", "ramen"}  
	nico := person{name: "nico", age: 18, favFood: favFood}  
	fmt.Println(nico.name)  
}  
  
package accounts  
  
// Account struct  
type Account struct {  
	owner   string  
	balance int  
}  
  
// NewAccount creates Account  
func NewAccount(owner string) *Account {  
	account := Account{owner: owner, balance: 0}  
	return &account  
}  
  
생성자 개념이 없기때문에 위 NewAccount에서 사용하는 패턴을 거의 사용한다.  
위 스트럭쳐에서 owner, balance는 소문자로 시작하기 때문에 초기화할 수 없다.  
대신 같은 패키지내의 NewAccount에서 생성하고 주소를 반환하면서 참조를 받는것이다.  
  
account := accounts.NewAccount("nico")  
  
이런식으로 호출하여 생성한다.  
accounts는 패키지 이름이다.  
  
// Deposit x amount on your account  
func (a Account) Deposit(amount int) {    // 앞에 괄호는 Receiver라는 녀석이다  
	a.balance += amount  
}  
  
// Balance of your account  
func (a Account) Balance() int {  
	return a.balance  
}  
  
스트럭쳐에 대한 메소드도 이렇게 구현할 수 있다.  
  
위에서 객체지향에 대한 실망을 날릴 수 있을것 같다.  
씨언어를 대체하기 위한 언어이지만 충분히 객체지향이 가능할거같다.  
  
상속이 없어도 캡슐화, 정보은닉 그리고 덕타이핑을 이용한 다형성정도는 가능할거 같다.  
  
Receiver의 이름은 컨벤션 룰로 실제 스트럭쳐의 소문자 첫글자로 시작해야한다.  
이름이 없는 함수에 인자로 a Account를 받고 Deposit(amount int) 함수를 리턴한다?  
이렇게 이해하면 좋을거같다.  
  
![]({{ site.url }}{{ site.baseurl }}/assets/images/2021-07-11-Golang syntax/dthumb-phinf.pstatic.net.png)이미지 썸네일 삭제  
  
**[go lang]포인터와 클래스개념 따라하기**  
[go lang]포인터와 클래스개념 따라하기  
  
그런데 잘봐보면 Deposit은 잘작동하지 않는다.  
c언어 기초를 생각해보면 알수있다. a는 복사본이다.  
  
func (a *Account) Deposit(amount int) {  
	a.balance += amount  
}  
  
익숙할 것이다. 저 매개변수의 *는 참조가 아니라 포인터를 의미한다.  
그리고 Balance의 경우에는 그렇다고하더라도 잘동작할것이다.  
func (a *Account) Withdraw(amount int) error {  
	if a.balance < amount {  
		return errNoMoney  
	}  
	a.balance -= amount  
	return nil  
}  
  
에러처리는 이런식으로 한다. 에러가 아닐떄 nil을 반환하는 것을 주목한다.  
  
	err := account.Withdraw(20)  
	if err != nil {  
		fmt.Println(err)  
	}  
	fmt.Println(account.Balance())  
  
그리고 에러를 직접 받아서 직접 코드를 작성해서 처리한다.  
try catch와 언어가 제공하는 exception객체등은 없어서 손수 작성한다.  
  
많이들 불만인거같다.  
하지만 아주 익숙하다. 회사에서 열심히 사람들이 하고있는짓이다.  
func (a Account) String() string {  
	return fmt.Sprint(a.Owner(), "’s account.\nHas: ", a.Balance())  
}  
  
이건 go에서 자동으로 호출해주는건데 ToString()같은 개념이다.  
  
package mydict  
  
import "errors"  
  
// Dictionary type  
type Dictionary map[string]string  
  
var errNotFound = errors.New("Not Found")  
  
// Search for a word  
func (d Dictionary) Search(word string) (string, error) {  
	value, exists := d[word]  
	if exists {  
		return value, nil  
	}  
	return "", errNotFound  
}  
  
type은 c의 typedef와 같은 개념인데 메소드를 가질 수 있다.  
어떤것이든 타입으로 어떠한 이름을 짓고 그것에 대한 메소드를 가질 수 있는 것이다.  
  
var (  
	errNotFound   = errors.New("Not Found")  
	errCantUpdate = errors.New("Cant update non-existing word")  
	errWordExists = errors.New("That word already exists")  
)  
  
여러 변수를 이렇게 초기화할 수도 있다  
  
파라메터의 경우,  
func (a, b int) Balance() int {  
	return a.balance  
}  
  
이런식으로 a, b int로 표현할 경우 둘 다 int형이다.  
  
func (a, b int) Balance() (int, int) {  
	return a.balance, 3;  
}  
  
그리고 (int, int)처럼 여러개의 반환값을 가질 수 있다.  
   
