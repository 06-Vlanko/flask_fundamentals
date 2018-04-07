from flask import Flask, render_template, redirect, request, session, jsonify
import random

app = Flask (__name__)
app.secret_key = 'dasecret'
randomNumber = random.randrange(0,101)


@app.route ('/')
def index():
    return render_template('index.html')

@app.route ('/process')
def process():
    number = request.args['guess']
    print 'The guessed number is ', number
    print 'The secret number is ', randomNumber
    if int(number) < randomNumber:
        return jsonify(val='too_low')
    elif int(number) > randomNumber:
        return jsonify(val='too_high')
    else:
        return jsonify(val='got_it')

@app.route ('/new_number')
def newNumber ():
    randomNumber = random.randrange(0,101)
    print 'The new secret number is ', randomNumber
    return redirect('/')
        


app.run(debug=True)