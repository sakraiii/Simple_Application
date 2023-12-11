from app import app
from flask import render_template, request, jsonify
import requests
import os, ssl


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    cardnumber = request.form['cardnumber']
    exdate = request.form['exdate']
    cvv = request.form['cvv']
    res1 = requests.post("https://tntwa4nlewy.SANDBOX.verygoodproxy.com/post",                   
                       json={'cardnumber': cardnumber, 'exdate': exdate, "cvv": cvv})
    return render_template('message.html', cardnumber=cardnumber, exdate=exdate, cvv=cvv)

@app.route("/forward", methods=['POST'])
def forward():
    cardnumber = request.form['cardnumber']
    exdate = request.form['exdate']
    cvv = request.form['cvv']

    os.environ['HTTPS_PROXY'] = 'https://US2b9hvnF1wE6g8bFHjQUn9G:1cc87476-74a8-4346-b3f1-b7e366794a21@tntwa4nlewy.SANDBOX.verygoodproxy.com:8443'
    res = requests.post("https://echo.apps.verygood.systems/post",
                        json={"cardnumber": cardnumber, "exdate": exdate, "cvv": cvv},
                        verify=False)                   
    res = res.json() 
    return render_template('forward.html', response=res)
