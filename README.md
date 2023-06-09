# 나의 웹페이지

<br>
<br>

## 작동목표


<br>

* Python의 flask라이브러리로 back-end를 구현하고 Html5, CSS, Javascript를 사용해 front-end를 구현
* Mysql DB를 이용하여 게시판 제작하기

<br>
<br>

## 개발환경


<br>

* Python, flask, Blueprint, request, Html5, CSS, Javascript, Bootstrap, Docker, Mysql

<br>
<br>

## 구동과정


![](https://github.com/gitcat87/WebPage/blob/main/images/capture1.png?raw=true)

#

<br>

```Python
#web.py
from flask import Flask,render_template,Blueprint,request,redirect,url_for
import pension as ds
from components import freeboard
import components.lotto4 as lotto4

app = Flask(__name__)

app.register_blueprint(freeboard.app)

@app.route("/")
def index():
    return render_template("/index.html")
```

```Html
<!-- index.html -->
{% extends 'base.html' %}

{%block video1%}
<script>
  document.addEventListener('DOMContentLoaded',()=>{
  const $dusrma = document.getElementById('dusrma')


  $dusrma.addEventListener('click',()=>{
    
  document.body.classList.toggle('reveal')
  setTimeout(()=>{window.location.href="/dusrma"},2000)
    })
    setTimeout(() => {
    document.body.classList.add("reveal")
}, 500)

  })

  
</script>
<div id="loader" style="z-index: 2">
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
</div>
<div id="bg-overlay"></div>
<video src="static/videos/video2.mp4"
autoplay muted loop id="bgvid-01">
</video>

{%endblock%}


{% block mainmenu%}

<h1 style="color: antiquewhite; text-shadow: -3px 3px red;">welcome to hompage!<br/> Click Anything You Want!</h1>
<div id="carouselExampleControls" class="carousel slide m-auto" data-bs-ride="carousel" data-interval="True">
    <div class="carousel-inner" >
      <div class="carousel-item active">
        <a href="lotto"><img src="/static/css/imgs/lotto.gif" style="width: 400px; height: 400px;" class="d-block  m-auto" alt="..."></a>
        <div class="carousel-caption d-none d-md-block">
          <h1>로또 당첨 확인</h1>
        </div>
      </div>
      <div class="carousel-item">
        <img src="/static/css/imgs/pension.gif" style="width: 400px; height: 400px; cursor: pointer;" class="d-block  m-auto" alt="..." id="dusrma">
        <div class="carousel-caption d-none d-md-block">
          <h1 style="color:black; font-weight: bold; cursor: pointer;">나의 연금은 얼마?</h1>
        </div>
      </div>
      <div class="carousel-item">
        <img src="https://picsum.photos/300/300/" class="d-block  m-auto" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" style="left: 500px;" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" style="right: 500px;" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
 
{% endblock%}

```

* 실행하면 flask 라이브러리로 지정해준 첫 root 주소로 접속하면 base.html에서 상속받은 index.html 을 사용자 화면에 렌더링을 합니다.

<br>
<br>


## BootStrap Carousel를 활용한 메뉴


![](https://github.com/gitcat87/WebPage/blob/main/images/capture8.gif?raw=true)

#

<br>

```html

<!-- index.html -->

{% block mainmenu%}

<h1 style="color: antiquewhite; text-shadow: -3px 3px red;">welcome to hompage!<br/> Click Anything You Want!</h1>
<div id="carouselExampleControls" class="carousel slide m-auto" data-bs-ride="carousel" data-interval="True">
    <div class="carousel-inner" >
      <div class="carousel-item active">
        <a href="lotto"><img src="/static/css/imgs/lotto.gif" style="width: 400px; height: 400px;" class="d-block  m-auto" alt="..."></a>
        <div class="carousel-caption d-none d-md-block">
          <h1>로또 당첨 확인</h1>
        </div>
      </div>
      <div class="carousel-item">
        <img src="/static/css/imgs/pension.gif" style="width: 400px; height: 400px; cursor: pointer;" class="d-block  m-auto" alt="..." id="dusrma">
        <div class="carousel-caption d-none d-md-block">
          <h1 style="color:black; font-weight: bold; cursor: pointer;">나의 연금은 얼마?</h1>
        </div>
      </div>
      <div class="carousel-item">
        <img src="https://picsum.photos/300/300/" class="d-block  m-auto" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" style="left: 500px;" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" style="right: 500px;" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
 
{% endblock%}

```

* Bootstrap의 carousel 코드를 사용하여 메인 메뉴를 꾸몄습니다.

<br>
<br>

## CSS를 활용한 로딩바


![](https://github.com/gitcat87/WebPage/blob/main/images/capture3.gif?raw=true)

#

<br>
<br>

### 로더바


```html
<!-- index.html -->
<div id="loader" style="z-index: 2">
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
</div>
```
<br>
<br>

```css
/* mystyle.css */

/* 부드러운 화면 전환 막대 애니메이션 시작*/
#loader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}
#loader > div {
    width: 100%;
    height: 12.5%;
    background: rgb(35, 53, 88);
    transition: transform 500ms;
}
#loader > div:nth-child(1) {
    transition-delay: 100ms;
}
#loader > div:nth-child(2) {
    transition-delay: 200ms;
}
#loader > div:nth-child(3) {
    transition-delay: 300ms;
}
#loader > div:nth-child(4) {
    transition-delay: 400ms;
}
#loader > div:nth-child(5) {
    transition-delay: 500ms;
}
#loader > div:nth-child(6) {
    transition-delay: 600ms;
}
#loader > div:nth-child(7) {
    transition-delay: 700ms;
}
#loader > div:nth-child(8) {
    transition-delay: 800ms;
}
body:not(.hidden).reveal #loader > div {
    transform: translateX(-100%);
}
/* 부드러운 화면 전환 막대 애니메이션 끝*/

```

<br>

* 페이지간 로딩으로 사용자 이탈방지 및 흥미유발을 위해 순차적으로 늘어났다가 줄어드는 로더바를 꾸몄습니다.

<br>
<br>

### 큐브

```html
<!-- base.html -->

    <div class="sk-cube-grid" style="z-index: 3; position: absolute;">
      <div class="sk-cube sk-cube1"></div>
      <div class="sk-cube sk-cube2"></div>
      <div class="sk-cube sk-cube3"></div>
      <div class="sk-cube sk-cube4"></div>
      <div class="sk-cube sk-cube5"></div>
      <div class="sk-cube sk-cube6"></div>
      <div class="sk-cube sk-cube7"></div>
      <div class="sk-cube sk-cube8"></div>
      <div class="sk-cube sk-cube9"></div>
    </div>
```

<br>

* 로더바가 동작하는 동안 출력되는 애니메이션 아이콘을 추가했습니다.

<br>
<br>

```css
/* mystyle.css */

/*로더 아이콘* 시작*/
.sk-cube-grid {
  left: 48%;
  top: 35%;
  width: 100px;
  height: 100px;
  margin: 100px auto;
  z-index: 3;
}

.sk-cube-grid .sk-cube {
    width: 33%;
    height: 33%;
    background-color: #ffffff;
    float: left;
    -webkit-animation: sk-cubeGridScaleDelay 1.3s infinite ease-in-out;
            animation: sk-cubeGridScaleDelay 1.3s infinite ease-in-out; 
  }
.sk-cube-grid .sk-cube1 {
-webkit-animation-delay: 0.2s;
        animation-delay: 0.2s; }
.sk-cube-grid .sk-cube2 {
-webkit-animation-delay: 0.3s;
        animation-delay: 0.3s; }
.sk-cube-grid .sk-cube3 {
-webkit-animation-delay: 0.4s;
        animation-delay: 0.4s; }
.sk-cube-grid .sk-cube4 {
-webkit-animation-delay: 0.1s;
        animation-delay: 0.1s; }
.sk-cube-grid .sk-cube5 {
-webkit-animation-delay: 0.2s;
        animation-delay: 0.2s; }
.sk-cube-grid .sk-cube6 {
-webkit-animation-delay: 0.3s;
        animation-delay: 0.3s; }
.sk-cube-grid .sk-cube7 {
-webkit-animation-delay: 0s;
        animation-delay: 0s; }
.sk-cube-grid .sk-cube8 {
-webkit-animation-delay: 0.1s;
        animation-delay: 0.1s; }
.sk-cube-grid .sk-cube9 {
-webkit-animation-delay: 0.2s;
        animation-delay: 0.2s; }

@-webkit-keyframes sk-cubeGridScaleDelay {
0%, 70%, 100% {
    -webkit-transform: scale3D(1, 1, 1);
            transform: scale3D(1, 1, 1);
} 35% {
    -webkit-transform: scale3D(0, 0, 1);
            transform: scale3D(0, 0, 1); 
}
}

@keyframes sk-cubeGridScaleDelay {
0%, 70%, 100% {
    -webkit-transform: scale3D(1, 1, 1);
            transform: scale3D(1, 1, 1);
} 35% {
    -webkit-transform: scale3D(0, 0, 1);
            transform: scale3D(0, 0, 1);
} 
}
/*로더 아이콘 끝*/
```

<br>
<br>

### 시계


![](https://github.com/gitcat87/WebPage/blob/main/images/capture10.gif?raw=true)

#

<br>

```html
<!-- base.html -->
      <div id="bottomclock-wrap">
        <div id="bottom-clock">지금 시간
             <h1 id="clock"></h1> 
            </div>
      </div>

```

<br>

```javascript
/* base.html */

        function getClock() {
          const d = new Date();
          const h = String(d.getHours()).padStart(2, "0");
          const m = String(d.getMinutes()).padStart(2, "0");
          const s = String(d.getSeconds()).padStart(2, "0");
          clock.innerText = `${h}:${m}:${s}`;
        }

        getClock(); //맨처음에 한번 실행
        setInterval(getClock, 1000); //1초 주기로 새로실행    

```

<br>

```css
/* mystyle.css */
#bottomclock-wrap>div{ 
    margin-right: 2rem;   
    display: flex; align-items: center;
}
#bottomclock-wrap{
    margin-left: auto;    
    color:azure
}
#bottom-clock{
    
    color: azure;
    display: flex; 
}
#bottom-clock>h1{
    display: flex;
    color: bisque;
    margin-left: 1rem;
}

```
<br>
* 웹 페이지를 이용하는 동안 시간을 확인 할 수 있도록 시계를 추가하였습니다.

<br>
<br>

## 로또 당첨 번호 확인


![](https://github.com/gitcat87/WebPage/blob/main/images/capture2.png?raw=true)

#

<br>
<br>

```python
#web.py

@app.route("/lotto",methods=['POST','GET'])
def lotto():
    turn = lotto4.turn[0].text
    number = lotto4.numbers[0].text
    number1 = lotto4.numbers[1].text
    number2 = lotto4.numbers[2].text
    number3 = lotto4.numbers[3].text
    number4 = lotto4.numbers[4].text
    number5 = lotto4.numbers[5].text
    potmoney = lotto4.potmoney[0].text
    bonus = lotto4.bonus[0].text
    potmoneyAll = lotto4.potmoneyAll
    date = lotto4.date[0].text
    howmany = lotto4.howmany[0].text
    thisweeknums = [number,number1,number2,number3,number4,number5]
    mynumpack = []
   
    cnt =1
    cnt2 = 0
    score = 0
    result = ["숫자가 등장합니다"]

    for i in range(6):        
        mynumpack += [request.args.get(f'mynum{cnt}')]
        cnt += 1
    
    
    for i in thisweeknums:
        if i == mynumpack[cnt2]:
            cnt2 += 1
            score += 1
        else:
            cnt2 += 1

    print(score)

    for i in range(1):
        if score == 6:
            result = '대박! 축하합니다! 1등 당첨입니다!'
            break
        if score == 5:
            result = '축하합니다! 2등 당첨!'
            break
        if score == 4:
            result = '축하합니다. 3등 당첨!'
            break
        if score == 3:
            result = '4등 당첨입니다.'
            break
        if score == 2:
            result = '5등 당첨입니다.'
            break
        else:
            result = '아쉽게도 낙첨입니다.'
            break


    print(result)

    return render_template("/lotto.html",number=number,
    number1=number1,number2=number2,number3=number3,number4=number4,number5=number5,
    turn=turn,potmoney=potmoney,bonus=bonus,potmoneyAll=potmoneyAll,date=date,howmany=howmany,result=result,mynumpack=mynumpack)
```

```python
#lotto4.py

import requests
from bs4 import BeautifulSoup
import time

url ="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="

req = requests.get(url)

req.encoding="euc-kr"

bs = BeautifulSoup(req.text,"html.parser")

turn =bs.select("#article > div:nth-child(2) > div > div.win_result > h4 > strong")
numbers= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span")
bonus= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span")
potmoney = bs.select("#article > div:nth-child(2) > div > table > tbody > tr> td:nth-child(4)")
date = bs.select('#article > div:nth-child(2) > div > div.win_result > p')
howmany = bs.select('#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')

potmoneyAll =[]

for i in potmoney:
    potmoneyAll += [i.get_text()]

potmoneyAll

```

<br>

* flask으로 mapping한 /lotto url주소로 접속하면 lotto4.py에 있던 코드를 바탕으로 웹 크롤링을 하고 갈무리 한 내용을 사용자 화면에 출력합니다.

<br>
<br>

## 나의 당첨 번호 확인하기

```python
#web.py
@app.route('/mynum',methods=['POST','GET'])
def mynum():
    mynum1 = request.form['Mynum0']
    mynum2 = request.form['Mynum1']
    mynum3 = request.form['Mynum2']
    mynum4 = request.form['Mynum3']
    mynum5 = request.form['Mynum4']
    mynum6 = request.form['Mynum5']   
    return redirect(url_for('lotto',mynum1=mynum1,mynum2=mynum2,mynum3=mynum3,mynum4=mynum4,mynum5=mynum5,mynum6=mynum6))
```


<br>

* redirect의 url_for()를 사용하여 사용자로부터 입력받은 파라미터 값을 lotto4.py에서 크롤링한 값과 비교 후 결과 값을 화면에 출력합니다.

<br>
<br>

## 게시판


![](https://github.com/gitcat87/WebPage/blob/main/images/capture11.png?raw=true)
![](https://github.com/gitcat87/WebPage/blob/main/images/capture6.png?raw=true)
![](https://github.com/gitcat87/WebPage/blob/main/images/capture7.png?raw=true)


#


```python

#freeboard.py

from flask import Blueprint, render_template, request, redirect
from components.db import freeboardmanage

app = Blueprint('freeboard', __name__, url_prefix='/freeboard')


@app.route('/view')
def view():
    idx = int(request.args.get('idx'))
    res = freeboardmanage.selectRow(idx)
    print(res)
    return render_template('freeboard/view.html', res=res)

@app.route("/board")
def board():
    page = request.args.get('page')
    page = 1 if page is None else page
    res = freeboardmanage.select(int(page))
    return render_template('freeboard/board.html', res=res)

@app.route("/updateform")
def updateform():
    idx = request.args.get('idx')
    res = freeboardmanage.selectRow(idx)
    return render_template('freeboard/updateform.html',res=res)

@app.route("/insertform")
def insertform():
    return render_template('freeboard/insertform.html')


@app.route("updateproc", methods=['POST'])
def updateproc():
    title = request.form['title']
    content = request.form['content']
    writer = request.form['writer']
    idx = request.form['idx']
    freeboardmanage.update(title,content,writer,idx)
    return redirect('/freeboard/board')

@app.route("insertproc", methods=['POST'])
def insertproc():
    title = request.form['title']
    content = request.form['content']
    writer = request.form['writer']
    freeboardmanage.insert(title,content,writer)
    return redirect('/freeboard/board')

@app.route("delete")
def delete():
    idx = int(request.args.get('idx'))
    freeboardmanage.delete(idx)
    return redirect('/freeboard/board')

```

```python
#freeboardmanage.py
import pymysql

host='192.168.0.66'
port=3306
user='root'
password='root123'
dbname='DHchoi'
charset='utf8'



def selectRow(idx):
    db = pymysql.connect(
        host=host, port=port,
        user=user, password=password,
        db=dbname, charset=charset
    )
    sql = f'select * from freeboard where idx = {idx}'
    
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    db.close()
    return res


def select(page):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    
    startrow = (page-1)*3
    # 1페이지면 startrow가 0
    # 2페이지면 startrow가 3
    # 3페이지면 startrow가 6
    
    sql = F'select * from freeboard order by idx desc limit {startrow},10'
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    print(res)
    return res


def update(title,content,writer,idx):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f"""UPDATE freeboard
                SET title = '{title}',
                    content = '{content}',
                    writer = '{writer}'
                WHERE idx ={idx};"""
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    print("update 수정해야함")

def insert(title,content,writer):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f"""INSERT INTO freeboard
            (title,content,writer,regdate)
            VALUES
            ('{title}','{content}','{writer}',NOW())"""
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    print("insert해야함")

def delete(idx):
    db = pymysql.connect(
        host=host,port=port,
        user=user,password=password,
        db=dbname,charset=charset
    )
    sql = f"""DELETE
             FROM freeboard 
            WHERE idx= {idx}"""
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    print("delete해야함",idx)

```
<br>
<br>

* 코드 유지보수 및 관리용이를 위하여 blueprint라이브러리를 활용, 같은 작업군을 묶어주었습니다.
* freeboard.py에서 mapping한 url 주소로 접속할 경우 freeboardmanage.py에 담긴 함수 내용들이 실행되고 다시 반환합니다.
* freeboardmanage.py에는 mysql서버로 보내기 위한 DB환경설정 정보와  SQL구문들이 담겨 있습니다. 이를 통해 CRUD를 수행 할 수 있습니다.

<br>
<br>

### 유효성 검사

![](https://github.com/gitcat87/WebPage/blob/main/images/capture5.png?raw=true)

#

<br>
<br>

```javascript

/* insertfom.html */
  <script>
    document.addEventListener('DOMContentLoaded',()=>{
    const $txar = document.getElementById('content-area')
    const $title = document.getElementById('title-area')
    const $writer = document.getElementById('writer-area')
    const $btn =document.getElementById('submit-btn')
    const $cancle = document.getElementById('cancle-btn');
    const h4 =document.querySelector('h4');
    const $form =document.querySelector('form');
    

    setTimeout(() => {
    document.body.classList.add("reveal");
    });

    $txar.addEventListener('click',()=>{
        $txar.textContent = ""       
    })
    $txar.addEventListener('keydown',()=>{
      $txar.textContent=""
    },{once:true})

    
    $cancle.addEventListener('click',()=>{
      window.location.href ="/freeboard/board"
    })


    $btn.addEventListener("click",(e)=>{    
      e.preventDefault();  // 기본 기능 막기
      if($title.value.length <1||$writer.value.length<1){
        alert('제목 또는 작성자에 내용이 필요합니다')
      }else{
        $form.submit()
      }
    })   

})
```

* null값이 입력되서 생기는 오류를 막기 위해 form에서 submit을 수행 할 때 이벤트 객체로 기본기능을 막고 값이 있을때만 전송하도록 작성했습니다.

<br>
<br>

## 연금 수령액 조회


![](https://github.com/gitcat87/WebPage/blob/main/images/capture9.png?raw=true)

#

<br>
<br>

```html
<!-- dusrma.html -->
<div id="dusrma-wrap">
  <div id="dusrmaInner-wrap">
    <h1 style="font-weight: 800;">당신의 미래,<img src="/static/css/imgs/dusrma.png" alt="">과 함께 하겠습니다.</h1>
    <hr>
  <div id="search-wrap">
    <h6 style="color: black; font-weight: bold; margin-right: 100px;">월 납입액을 입력하세요</h6>
    <form action="/dusrma" method="POST">    
    <input type="text" id="pension-input" name="pension" value="{{pension}}">
    <input type="submit" value="예상 연금 수령액 확인" id="search-btn">
  </form>
  </div>
  <div id="result-wrap">
    <div>{{result[0]}}</div>
    <div>{{result[1]}}</div>
    <div>{{result[2]}}</div>
    <div>{{result[3]}}</div>
    <div>{{result[4]}}</div>
    <div>{{result[5]}}</div>
  </div>
  <hr>
  <h1 style="text-align: left; width: 90%; margin-left: auto; margin-right: auto; margin-top: 2rem; font-weight: 1000; font-family: sans-serif;">잠깐만요! 반드시 확인하세요!</h1>
  <div id="readme-wrap">   
    <div id="readme">
      <p>① 연금액 = 기본연금액 * 지급률 + 부양가족연금액<br/>
        *(기본연금액) {1.275*(A+B)*P18/P+...+1.2*(A+B)*P23/P}(1+0.05n/12)<br/>
        -A-연금수급 전 3년간 전체 가입자의 평균 소득월액의 평균액<br/>
        -B-가입자 개인의 가입기간 중 기준소득월액의 평균액, n-20년 초과 가입 월수<br/>
        -P-전체 가입 월수, P16~P23-연도별 가입월수<br/><br/>
        *(지급률)<br/>
        -노령연금의 지급률 : 가입기간 10년 기준 50%에 가입기간 1년을 초과하는 1년마다 5%를 가산 (1년 미만이면 매 1개월 마다 5/12% 가산), 20년이상 100%<br/>
        -장애연금의 지급률 : 장애1급 100%, 2급 80%, 3급 60%, 40급(일시금) 225%<br/>
        -유족연금의 지급률 : 사망자의 가입기간 10년 미만 40%, 10년 이상 20년 미만 50%, 20년 이상 60%<br/><br/>
        *(부양가족연금액) 배우자 연 283,380원, 자녀/부모 1인당 연 188,870원<br/>
        ② 월 납입보험료는 사업장가입자의 경우 본인 기여금과 사업장 부담금을 합산한 금액 기준임<br/>
        ③ 연금의 월지급액(부양가족연금액 포함)은 가입자이었던 최종 5년간의 기준소득월액의 평균액과 가입기간중의 기준소득월액의 평균액을 재평가한 금액 중에서 많은 금액을 초과하지 못합니다.<br/>
        ④ 장애연금액은 가입기간 20년이하 기준이며, 20년을 초과할 경우 가입기간에 비례하여 연금액이 증가됨.<br/>
        ⑤ 가입기간 20년 초과시 유족연금액은 20년가입시를 기준으로 가입기간에 비례하여 연금액이 증가됨.<br/>
        ⑥ 2023년 1월부터 최초 가입 및 “A”값(2023년도 적용 2,816,091원)을 가정하여 산정하였으므로 실제와 상이할 수 있습니다.</p>
    </div>
  </div>
</div>
</div>
```

```css
/* dusrma.html */
<style>

  #dusrma-wrap{
    height: 65vh;

    display: flex; justify-content: center;
    
  }
  #dusrmaInner-wrap{
    width: 55%;
    background-color:rgba(250, 218, 218, 0.4);
    font-family: sans-serif;
  }
  #pension-input{
    width: 200px;
    height: 50px;
    border-radius: 0.2rem;
    border: transparent;
    font-size: 25px;
    font-family: sans-serif;
    box-shadow: 1px 1px 5px 1px rgba(0, 0, 0, 0.37);
   
    
  }
  #search-wrap{
    padding: 0;
    display: flex; justify-content: center; align-items: center;
    
  }
  #search-btn{
    width: 150px;
    height: 50px;
    border-radius: 0.2rem;
    border: none;
    background-color: rgb(53, 52, 52);
    color: white;
    margin-left: 1rem;
  

  }
  #result-wrap{
    margin-top: 1rem;

    display: flex; justify-content: center;
    font-size: 25px;    
  }
  #result-wrap>div{
    width: 200px;
    height: 50px;
    border-radius: 0.2rem;
    display: flex; align-items: center; justify-content: center;
    background-color: white;
    margin-left: 1rem;
    margin-right: 1rem;
    font-family: sans-serif;
    box-shadow: 1px 1px 5px 1px rgba(0, 0, 0, 0.37);
  }
  #readme-wrap{
  
    margin-left: auto;
    margin-right: auto;
    border: 1px solid rgba(71, 71, 71, 0.329);
    width: 90%;
    height: 30%;
    background-color: rgba(255, 255, 255, 0.8);
    box-shadow: 1px 1px 5px 1px rgba(0, 0, 0, 0.37);
    overflow-y: scroll;
  }
  #readme{
    text-align: left;
  }
  #readme>p{
    font-family: sans-serif;
    font-weight: 800;
  }
</style>
```
<br>
<br>

```python
#pension.py

from bs4 import BeautifulSoup
import requests

def dusrma(insu):
    url  = f'https://www.nps.or.kr/jsppage/app/etc/simpleExpect.jsp?yyyy=2022&status=cal&max=471600&min=29700&insu={insu}&inquiry=%BF%B9%BB%F3%BF%AC%B1%DD%BE%D7+%C1%B6%C8%B8%C7%CF%B1%E2'
    req = requests.get(url)
    req.encoding = "utf-8"
    html = BeautifulSoup(req.content,"html.parser")
    data_1 = html.select("span.data")
    years10 = data_1[0].string
    years15 = data_1[1].string
    years20 = data_1[2].string
    years25 = data_1[3].string
    years30 = data_1[4].string
    years35 = data_1[5].string
    years40 = data_1[6].string
    b = [years10+"원",years15+"원",years20+"원",years25+"원",years30+"원",years35+"원",years40+"원"] 
    return b
```

```python
#web.py
@app.route('/dusrma',methods=['POST','GET'])
def pension():
    if request.method == 'POST':
        insu = request.form['pension']
    else:
        insu = 330000
    result = ds.dusrma(insu)
    print(result)
    return render_template('/dusrma.html',result=result,pension=insu)
```

<br>
<br>

* 사용자가 입력한 값을 바탕으로 웹 크롤링을 수행하여 원하는 결과를 출력합니다.
* 납입 연금액을 기입하면 기입한 숫자를 바탕으로 연금 홈페이지에서 조회하여 request와  beautifulsoup로 크롤링하여 데이터를 가져옵니다.

<br>
<br>


## 그 외 디자인적 요소


![](https://github.com/gitcat87/WebPage/blob/main/images/capture12.gif?raw=true)
![](https://github.com/gitcat87/WebPage/blob/main/images/capture13.gif?raw=true)

#

<br>
<br>

```javascript

/* base.html*/
/* 마우스 오버 마우스 아웃 글자 변화 */
        notice.addEventListener("mouseover", () => {
          noticeh1.textContent = "What's New?";
        });

        notice.addEventListener("mouseout", () => {
          noticeh1.textContent = "Board";
        });

```
<br>
<br>

```javascript
/* lotto.html */
/* 마우스 오버 마우스 아웃 글자 색 변화*/
  document.addEventListener("DOMContentLoaded", () => {
    const $h1 = document.querySelector("#lotto-title");
    const $numbers = document.querySelectorAll('.number')
    const $input =document.querySelectorAll('.inputnumber')
    
    
    const $formbtn = document.getElementById('formbutton').addEventListener('click',()=>{
        $h2 = document.getElementById('ckresultH1').style.visibility = 'visible'
        
    })
...
...
...
...
    $numbers.forEach((num)=>{
      num.addEventListener("mouseover",(e)=>{
        /*console.log("올렸음")*/
        e.target.style.color="red"
      })
    })
        $numbers.forEach((num)=>{
      num.addEventListener("mouseout",(e)=>{
        e.target.style.color="white"
      })
    })

  })

```

<br>
<br>

```javascript
/* lotto.html*/
/* setinterval로 글자색을 반짝이는 듯한 효과 주기*/

    setInterval(() => {
      $h1.style.color = "red";
      $h1.style.fontsize;
    }, 100);
    setInterval(() => {
      $h1.style.color = "green";
    }, 200);

    setInterval(() => {
      $h1.style.color = "orange";
    }, 300);

```

* javascript로 다양한 디자인 효과를 주었습니다.


