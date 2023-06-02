from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notice')
def board():
    return render_template('notice.html')


app.run(debug=True)