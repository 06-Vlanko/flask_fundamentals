from flask import Flask, render_template, redirect, request, flash, session
app = Flask (__name__)
app.secret_key = 'awesomesecret'

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    needsRedirect = False
    name = request.form['name']
    location = request.form['dojo-location']
    fav_lang = request.form['fav-lang']
    comment = request.form['comment']
    if len(name)<1:
        flash ('Name cannot be empty!')
        needsRedirect = True
    if len(comment)<1:
        flash ('Comment cannot be empty')
        needsRedirect = True
    elif len(comment)>=120:
        flash ('Comment cannot exceed 120 characters')
        needsRedirect = True
    if needsRedirect:
        return redirect('/')

    return render_template ('result.html', name=name, location=location, fav_lang=fav_lang, comment=comment)

app.run(debug=True)