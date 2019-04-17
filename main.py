from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods= ['POST','GET'])
def index():

    username = ''
    email = ''
    username_error = ''
    password1_error = ''
    password2_error = ''
    email_error = ''
    title = 'Registration'

    if request.method == 'POST':

        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        email = request.form['email']
        counta = 0
        countdot = 0
        countuserspace = 0
        countpwspace = 0
        
        if username != '':
            for i in username:
                if i == " ":
                    countuserspace += 1
            if countuserspace != 0:
                username_error = 'Spaces are not allowed in usernames.'
                username = ''
            else:
                if len(username) < 3 or len(username) > 20:
                    username_error = 'Username must be between 3 and 20 characters'
                    username = ''
        else:
            username_error = 'Username cannot be blank'



        if password1 != '':
            for i in password1:
                if i == " ":
                    countpwspace += 1
            if countpwspace != 0:
                password1_error = 'Spaces are not allowed in passwords.'
                password1 = ''    
            else:
                if len(password1) < 3 or len(password1) > 20:
                    password1_error = 'Password must be between 3 and 20 characters'
                    password1 = ''        
            if password2 != password1:
                password2_error = 'Passwords do not match. Re-enter password and confirmation.'
                password1 = ''
                password2 = ''
        else:
            password1_error = 'Password cannot be blank.'
        
        if email != '':
            for i in email:
                if i == '@':
                    counta += 1
                if i == '.':
                    countdot += 1
            if counta != 1 or countdot !=1:
                email_error = 'email format issue: must have one "@" and one "."'
                email = ''
     
        if (not username_error) and (not password1_error) and (not password2_error) and (not email_error):
            return redirect('/feedback?username={0}'.format(username))


    return render_template('signup_form.html', title=title, username=username, 
                           username_error=username_error, password1_error=password1_error,
                           password2_error=password2_error, email=email, email_error=email_error)

@app.route('/feedback')
def feedback():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('feedback.html', title=title, username=username)

app.run()