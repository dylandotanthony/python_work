import re
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models import user
from flask_app.models import band
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# Login & Reg page
@app.route('/')
def index():
    return render_template("index.html")

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Create
@app.route('/register/user', methods=['POST'])
def register():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        # put the pw_hash into the data dictionary
        "password" : bcrypt.generate_password_hash(request.form['password'])
        }
    a_user = user.User.create_user(data)
    # store user id into session
    session['user_id'] = a_user
    flash('Registration Successful!', "register")
    return redirect('/dashboard')

# Login 
@app.route("/login", methods=["POST"])
def login():
    if not user.User.validate_login(request.form):
        return redirect("/")
    a_user = user.User.get_by_email(request.form)
    if a_user:
        if not bcrypt.check_password_hash(a_user.password, request.form["password"]):
            flash("Email/Password combination is incorrect")
            return redirect("/")
        session['user_id'] = a_user.id
        # flash("Login was successful!")
        return redirect("/dashboard")
    flash("Email is not tied to an account")
    return redirect("/")

# @app.route("/account")
# def user_detail():
#     if "user_id" not in session:
#         return redirect('/')
#     data ={
#         'id': session['user_id']
#     }
#     get_bands = band.Band.get_all_bands_with_user(data)
#     return render_template("edit.html", bands=get_bands, user=user.User.get_by_id(data))

@app.route("/update/<int:user_id>", methods=['POST'])
def edit_user(user_id):
    valid_user = user.User.validate_update(request.form) 
    if not valid_user:
        return redirect(f'/account/{user_id}')
    return redirect('/dashboard')


@app.route("/show")
def user_detail():
    if "user_id" not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    a_band = band.Band.get_all_bands_with_user(data)
    
    return render_template("show.html",a_band=a_band, user=user.User.get_by_id(data))