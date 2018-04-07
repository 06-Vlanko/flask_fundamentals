from flask import Flask, render_template, redirect, request, session

app = Flask (__name__)
app.secret_key = 'super-secret'

@app.route ('/')
def index ():
    print session ['counter']
    session['counter'] = session['counter'] + 1
    return render_template ('index.html', number=session['counter'])

@app.route ('/process')
def process():
    session['counter'] = session['counter'] + 1
    return redirect ('/')

@app.route ('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')
app.run(debug=True)