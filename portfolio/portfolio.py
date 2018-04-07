from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')

def index ():
    return render_template('index.html')


@app.route('/projects')
def project ():
    return render_template('projects.html')

@app.route('/aboutme')
def aboutMe():
    return render_template('about.html')

app.run(debug=True)