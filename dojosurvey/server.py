from flask import Flask, render_template, redirect, request
app = Flask (__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print 'hi!'
    name_ = request.form['name']
    location_ = request.form['dojo-location']
    fav_lang_ = request.form['fav-lang']
    comment_ = request.form['comment']

    print name_, location_, fav_lang_, comment_

    return render_template ('result.html', name=name_, location=location_, fav_lang=fav_lang_, comment=comment_)

app.run(debug=True)