from flask import Flask, render_template, redirect, request
app = Flask (__name__)

@app.route ('/')
def index():
    return render_template ('index.html')

@app.route ('/ninja')
def ninja():
    return render_template ('ninja.html')

@app.route('/ninja/<landing>')
def show(landing):
    print '-------------------------------'
    print landing
    print '-------------------------------'
    if landing == 'blue':
        return render_template ('ninja_blue.html')
    elif landing == 'orange':
        return render_template ('ninja_orange.html')
    elif landing == 'red':
        return render_template ('ninja_red.html')
    elif landing == 'purple':
        return render_template ('ninja_purple.html')
    else:
        return render_template ('not_april.html')

app.run (debug=True)