from flask import Flask, render_template, redirect, request, session, flash
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask (__name__)
app.secret_key = 'onesecret'

@app.route ('/')
def index():
    return render_template ('index.html')

@app.route ('/process', methods=['POST'])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    date = request.form['date']
    
    #flag that will decide if a redirect is required
    needsRedirect = False

    #checks if any fields were left empty + other verifications

    if len(first_name)<1:
        needsRedirect = True
        flash ('The "First Name" field cannot be empty')
    else: #verifies if all characters in first_name are letters
        for character in first_name:
            if not character.isalpha():
                needsRedirect = True
                flash ('The "First Name" field should only contain letters')
                break

    if len(last_name)<1:
        needsRedirect = True
        flash ('The "Last Name" field cannot be empty')
    else: #verifies if all characters in last_name are letters
        for character in last_name:
            if not character.isalpha():
                needsRedirect = True
                flash ('The "Last Name" field should only contain letters')
                break
    
    if len(email)<1:
        needsRedirect = True
        flash ('The "Email" field cannot be empty')
    #checks if the email is in the format something@something.some
    elif not EMAIL_REGEX.match(email):
        needsRedirect = True
        flash ("Invalid email address")

    if len(password)<1:
        needsRedirect = True
        flash ('The "Password" field cannot be empty')
    #checks the length of the value entered in the password field, if its less than 8 redirects
    elif len(password)<=8:
        needsRedirect = True
        flash ('The password must be more than 8 characters')
    #checks if the password field has at least 1 uppercase letter and 1 number
    else:
        hasUpper = False
        hasNumber = False
        for character in password:
            #checks for uppercases
            if character.isupper():
                hasUpper = True
            if character.isdigit():
                hasNumber = True
        if not hasUpper:
            needsRedirect = True
            flash ('Your password must contatain at least one uppercase letter')
        if not hasNumber:
            needsRedirect = True
            flash ('Your password must contatain at least one number')
    if len(confirm_password)<1:
        needsRedirect = True
        flash ('The "Confirm Password" field cannot be empty')
    #checks that the password and confirm password lengths match
    if len(password) != len(confirm_password):
        needsRedirect = True
        flash ('The password and confirm password values should match')
    else: #if the lengths match, check if characters are an exact match
        for index in range ( len(password) ):
            if password[index] != confirm_password[index]:
                needsRedirect = True
                flash ('The password and confirm password values should match')
                break
    if len (date) < 1:
        flash ('The "Date of Birth" field cannot be empty')
    else:
        #splits the user entered date
        month, day, year = date.split('/')
        try: #if the date is not valid the following line will cause an exception (error)
            datetime.datetime(year=int(year),month=int(month),day=int(day))
        except ValueError: #this will catch the error and take action cuz the date was invalid
            print '-----> Got errors'
            needsRedirect = True
            flash ('The date you entered is not valid, please enter a valid date with format mm/dd/yyyy')
        
    if needsRedirect:
        needsRedirect = True
        print 'redirecting cuz missing'
        return redirect ('/')
    else:
        print 'redirecting with success'
        flash ('Success!!!')
        return redirect ('/')

app.run (debug = True)