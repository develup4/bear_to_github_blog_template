---
title:  Linux command

categories: Linux 
tags: CLI
 
---

  
  
  
  
pwd : print working directory  
/ : root directory  
~ : home directory  
cd : change directory  
--help : simple manual  
ㅁman command : manual  
ls -l : list in long format  
touch L make empty file  
.filename : hidden files  
ls -a : show all files    // 히든파일 조회가능  
ls -al  
mkdir : make directory  
./ : current directory  
mv : move(rename)  
rm -r : remove directory    // -r은 recursive라는 뜻응로 내부 directory까지   
../ : parent directory  
  
mkdir dummy; cd dummy; touch hello.txt; cd ..; ls -R    // 순차실행  
mkdir dummy && cd dummy && touch hello.txt && cd ..&& ls -R    // 실패하면 멈추기  
htop (메모리 하드 등등   
  
top은 기본설치되어있는데 윈도우의 작업관리자같은걸로 프로세스 사용량등을 파악할 수있다.  
  
htop은 더 좋은거  
  
​  
  
vmstat (가상메모리 조회?)  
  
​  
  
apt-get이나 yum등의 패키지 매니저를 통해 받을 수 있다.앱스토어같은거다  
  
apt-get update  
등을 통해 목록을 업데이트받을 수 있다.  
  
​  
  
맥에서는 homebrew를 통해 가능  
  
​  
  
기본중에 기본이지만 빠진것도 있었다.그리고 이런 명령어들으이 표준도 posix인줄 몰랐다. std lib의 표준인줄  
  
근데 이런 명령어 하나하나도 프로그램이다. 명령인자로main의 arg가 되는  
  
​  
  
​  
  
mkdir -p dir1/dir2/dir3  
man보면 다 나오지만 이렇게 중간에dir2가 없다던지해도 -p로 하면 다 생성해준다(--parent)  
  
​  
  
man [커맨드]  
커맨드에 대한 매뉴얼이 출력되며 방향키로 위아래로 움직일 수 있고  
  
이상태에서 슬러쉬(/)를 누르고 키워드를 쓰면 검색이 된다 /mode  
  
​  
  
그 상태에서 n키로 다음으로 넘어갈 수 있으며,  
  
q키로는man을 빠져나갈 수잇다  
  
​  
  
​  
  
wget -o [저장할 파일명] [url]  
wget으로는 cli환경에서 다운을 받을 수 있다. 소셜네트워크 오프닝에서도 나온다.  
  
​  
  
​  
  
​  
  
파이프라인  
  
하나의 프로세스의 결과를 다른 프로세스의 인풋으로 받아서 계속 연결시키는것  
  
​  
  
cat [파일내용]  
파일내용을 출력  
  
​  
  
grep => grep은 어떤 특정한 정보에서 원하는 정보가 포함된 행을 출력하는 명령어  
  
​  
  
ls --help | grep sort  
ls --help의 출력결과를 파이프(|)로 연결해서 grep의 인풋으로 넘겨주고 grep은 sort가 포함된 행을 출력한다.  
  
​  
  
​  
  
​  
  
​  
  
​  
  
ps aux  
  
실행중인 프로세스 출력  
  
​  
  
​  
  
​  
  
​  
  
​  
  
​  
  
​  
  
​  
  
https://opentutorials.org/course/2598/14199  
  
   
IO Redirection - 생활코딩  
IO Redirection 2016-11-26 10:35:24 강의 output input  안 중요한 이야기들 댓글을 작성하려면 로그인하셔야 합니다. spidoid 2개월 전 outptut 영상에서 나온 참고 사이트 주소입니다. Lecture 6 - shell scripting http://slideplayer.com......304 J 3개월 전 08.21.20 완료 홍주호 6개월 전 20.5.31 복습 홍주호 7개월 전 20.5.22 완료 개발벌레 7개월 전 언제 한 번 써 봐야겠네요. 뎨르릅 10개월 전 목소리 왤케 친절하십...  
  
opentutorials.org  
  
생활코딩 IO redirection부터 안봣음  
  
​  
  
​  
  
​  
  
​  
  
awk, sed, lsof, curl, less, find, kill 등도 정리해야함  
  
​  
  
​  
  
​  
  
​  
  
io redirection  
  
​  
  
ls -al > output.txt  
기본적으로 stdout 또는 에러메시지의 경우 stderr로 출력이 되지만 >를 통해 출력의 방향을 리다이렉션 할수 있다.  
  
위의 경우 파일에 출력  
  
​  
  
출력스트림번호> 가 기본 형식인데 생략시 1번이다. 즉 1> 이건데 생략하고 >로 쓸수있고 1은 stdout이다.  
  
에러 출력시에는  
  
ls -al 2> output.txt  
이런식으로 사용해야 한다.  
  
​  
  
rm aa.txt 1> result.txt 2> error.log  
이렇게 출력스트림을 여러개 지정할수도 있다. 에러가 출력된다면(aa.txt가 없다던지) error.log 파일에 출력될거시앋.  
  
​  
  
cat  
aa  
aa  
bbb  
bbb  
이렇게 cat 뒤에 아무 인자도 주지않으면 키보드 인풋을 받아서 엔터를 치면 그대로 다시 출력이 된다.(stdin)  
  
​  
  
cat < hello.txt  
사실 cat의경우 <를 생략해도 똑같이 동작하지만, 아무튼 이런식으로 input redirection도 가능하다.  
  
​  
  
head -n1 < linux.txt > out.txt  
이렇게 i/o를 동시에 지정할수도 있다. linux.txt의 첫줄이 out.txt에 출력될것이다. 참고로 -n1은 첫 한줄만 출력하는 옵션이다.  
  
​  
  
입출력을 할때 그 장소에 이미 내용이 있을때 redirection은 기본적으로 덮어쓰기인데 append를 하고싶다면 >>이나 <<를 쓴다.  
  
ls -al >> output.txt  
이렇게 쓰면 기존에 output.txt에 내용이 있을때 내용이 append된다.  
  
​  
  
cat << hello.txt << aa.txt  
이렇게 여러 인풋을 이어서 append할수도 잇따.  
  
​  
  
  
​  
  
​  
  
> ps aux    
ps는 프로세스를 보는 커맨드이고 aux로 모두 다 볼 수 있따.  
  
​  
  
ps aux | grep apache  
이렇게 파이프를 통해 원하는 프로세스를 확인할 수 있고,  
  
​  
  
sudo kill 1599  
이런식으로 표시된 pid를 적어서 프로그램을 킬할수도 있다.  
  
​  
  
​  
  
아무 경로에서나 ls와 같이 명령을 실행할 수 있는 것은 환경변수때문이다(윈도우랑 마찬가지)  
  
$PATH에 환경변수들이 저장되어 있으며  
  
​  
  
echo $PATH  
  
로 확인가능  
  
​  
  
​  
  
whereis 위치표시  
  
find 실제 디렉토리를 찾아서 실제검색  
  
locate 인덱싱같은게 되어있어서 정리된정보에서 빠르게 검색(부정확가능 => 더찾아보기)  
  
​  
  
help find | head  
  
이렇게도 파이프로 사용가능  
  
​  
  
​  
  
ctrl + z로 현재 프로세스를 백그라운드로 보낼 수 있따.  
  
jobs명령으로 백그라운드 프로세스를 확인할 수 있고 거기 번호대로  
  
​  
  
fg %3이런식으로 3번 백그라운드로 돌아갈 수 있고  
  
fg만하면 스택에서 제일 높은애로 복귀한다.  
  
​  
  
kill %3도 가능하고  
  
​  
  
​  
  
어떤 명령  
  
ls -alR > result.txt &  
  
이런식으로 마지막에 앤퍼센트를 붙이면 바로 백그라운드로 실행한다.  
  
​  
  
​  
  
daemon 백그라운드에서 항상 실행되어있는 프로그램  
  
/etc/init.d에 데몬 프고글매들 이 있ㅇ므ㅕ  
  
실행은  
  
sudo service 이름 start / stop으로 중지  
  
​  
  
데몬은 부팅시 바로 실행되야한느 경우가 많은데 설정법은  
  
/etc/rc3.d(cui)  
  
/etc/rc5.d(gui)에 링크(바로가기)를 추가해서 설정한다.  
  
링크의 예는 S02Apache2  
  
여기서 02는 우선순위이다  
  
​  
  
​  
  
​  
  
​  
  
​  
  
​  
  
crontab -e로 에디터에 추가해서 주기적으로 실행하는 프로세스를 추가할 수 잇다.  
  
​  
  
  
​  
  
ex  
  
1/* * * * * * * date >> date.log 2>&1  
  
>>는 append이며, 2>&1은 에러 출력을 표준출력으로 리다이렉트한다는 의미  
  
​  
  
tail -f date.log  
  
=>계속 실행되있으면서 data.log에변화가 있으면 출력됨. 실시간 로그확인용  
  
​  
  
크론의 활용예로  
  
서버에서는 응답을 바로주고 실제 처리는 모아서 주기적으로 한다던지 이런것이 가능하다.  
  
​  
  
​  
  
​  
  
​  
  
​  
  
​  
  
​  
  
shell실행시 자동실행  
  
~ 경로에서 bashrc에 쉘스크립트 추가  
  
​  
  
(ex) alias c='clear'  
  
alias는 재부팅시 리셋되므로 설정하면 편하다.  
  
  
  
  
grep  
awk  
sed  
lsof  
curl  
wget  
tail  
head  
less  
find  
ssh  
kill  
sort  
uniq  
cat  
cut  
echo funt  
tr  
nl  
egrep  
fgrep  
wc  
ps  
top  
htop  
atop  
nmap  
tcpdump  
ping  
mtr  
traceroute  
dig  
airmon  
airodump  
iptables  
netstat  
nmon  
iostat  
sar  
vmstat  
strace  
dtrace  
systemtap  
uname  
df  
history  
  
​  
