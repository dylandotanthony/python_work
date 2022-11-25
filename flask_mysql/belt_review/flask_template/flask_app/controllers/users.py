import re
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session.clear()
    # session['user_id'] = None
    return redirect('/')

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    if not User.validate_registration(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
        }
    # Call the save @classmethod on User
    user_id = User.register_user(data)
    # store user id into session
    session['user_id'] = user_id
    flash('Registration Successful!')
    return redirect("/dashboard")


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not User.validate_login(request.form):
        return redirect('/')
    # see if the username provided exists in the database
    if user:
        # if user exists, check if password matches
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            # if password does not match
            flash("Email/Password is incorrect")
            return redirect('/')
        # if password does match 
        session['user_id'] = user.id
        flash('Login was successful')
        return redirect('/success')
    flash("Email is not tied to an account")
    return redirect('/')