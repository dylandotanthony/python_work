import re
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models import user
from flask_app.models import magazine
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
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        # put the pw_hash into the data dictionary
        "password" : bcrypt.generate_password_hash(request.form['password'])
        }
    user = User.create_user(data)
    # store user id into session
    session['user_id'] = user
    flash('Registration Successful!', "register")
    return redirect('/dashboard')


@app.route("/login", methods=["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect("/")
    user = User.get_by_email(request.form)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            flash("Email/Password combination is incorrect")
            return redirect("/")
        session['user_id'] = user.id
        flash("Login was successful!")
        return redirect("/dashboard")
    flash("Email is not tied to an account")
    return redirect("/")

@app.route("/account/")
def user_detail():
    if "user_id" not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    Magazine = magazine.Magazine
    get_magazines = Magazine.get_by_magazine(data)
    return render_template("update.html",get_magazines=get_magazines)

    # magazine_data = {
    #     'id': user_id
    # }
    # magazine =[]
    # user=User.get_by_id(data)
    # magazine=Magazine.get_by_id(magazine_data)

@app.route("/update/<int:user_id>", methods=['POST'])
def edit_user(user_id):
    valid_user = User.validate_update(request.form) 
    if not valid_user:
        return redirect(f'/account/{user_id}')
    return redirect('/dashboard')