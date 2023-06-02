from flask import Flask,render_template,Blueprint,request,redirect,url_for
import pension as ds
from components import freeboard
import components.lotto4 as lotto4

app = Flask(__name__)

app.register_blueprint(freeboard.app)

@app.route("/")
def index():
    return render_template("/index.html")



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

@app.route('/mynum',methods=['POST','GET'])
def mynum():
    mynum1 = request.form['Mynum0']
    mynum2 = request.form['Mynum1']
    mynum3 = request.form['Mynum2']
    mynum4 = request.form['Mynum3']
    mynum5 = request.form['Mynum4']
    mynum6 = request.form['Mynum5']   
    return redirect(url_for('lotto',mynum1=mynum1,mynum2=mynum2,mynum3=mynum3,mynum4=mynum4,mynum5=mynum5,mynum6=mynum6))

@app.route('/dusrma',methods=['POST','GET'])
def pension():
    if request.method == 'POST':
        insu = request.form['pension']
    else:
        insu = 330000
    result = ds.dusrma(insu)
    print(result)
    return render_template('/dusrma.html',result=result,pension=insu)

app.run(debug=True,host="0.0.0.0")