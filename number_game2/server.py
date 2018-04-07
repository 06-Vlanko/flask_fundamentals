from flask import Flask, render_template, redirect, request, session
import random

app = Flask (__name__)
app.secret_key = 'thissecret'

@app.route ('/')
def index():
    if session['number'] == None:
        session['number'] = random.randrange(0, 101)
        print session
    print session
    return render_template ('index.html')

@app.route ('/process', methods=['POST'])
def process ():
    print "Got Post Info"
    print 'woeiweoi'+request.form['number']
    if (session['number']==request.form['number']):
        print 'Its a match!'
    return redirect ('/')

app.run(debug=True)