from flask import Flask,render_template,request,redirect, url_for
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


url ="https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="

req = requests.get(url)

req.encoding="euc-kr"

bs = BeautifulSoup(req.text,"html.parser")

turn =bs.select("#article > div:nth-child(2) > div > div.win_result > h4 > strong") #회차
numbers= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span") #당첨번호 6자리
bonus= bs.select("#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span") #당첨번호 보너스
potmoney = bs.select("#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(4)") #당첨금


turnValue = turn[0].text #회차.텍스트
numbersValue = (numbers[0].text,numbers[1].text,numbers[2].text,numbers[3].text,numbers[4].text,numbers[5].text)
bonusValue = bonus[0].text
potmoneyValue = potmoney[0].text






@app.route('/')
def index():
    numbersValue
    return render_template('/index.html',numbersValue=numbersValue)



@app.route('/lotto',methods=['POST'])
def lotto():
    count = 0
    dingdongdang= []
    score = 0
    result = None
    numbersValue
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    num4 = request.form['num4']
    num5 = request.form['num5']
    num6 = request.form['num6']
    numbers=[num1,num2,num3,num4,num5,num6]
    
    for i in numbersValue:
        if i == numbers[count]:
            dingdongdang += "O"
            score += 1
        else:
            dingdongdang += "X"
        count += 1
    print(dingdongdang)
    print(score)

    for i in range(score+1):
        if score == 6:
            print('1등입니다!')
            result = "1등입니다"
            break
        if score == 5:
            print('2등입니다!')
            result = "2등입니다"
            break
        if score == 4:
            print('3등입니다!')
            result = "3등입니다"             
            break
        if score == 3:
            print('4등입니다!')
            result = "4등입니다"
            break
        if score == 2:
            print('5천원~')
            result = "5천원입니다"
            break
        else:
            print('아쉽네요')
            result = "아쉽습니다"
        
    
 
    return render_template('/index.html',num1=num1,num2=num2,num3=num3,num4=num4,num5=num5,num6=num6,numbersValue=numbersValue,dingdongdang=dingdongdang)

app.run(debug=True)