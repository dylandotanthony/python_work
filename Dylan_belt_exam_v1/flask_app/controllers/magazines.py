from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.magazine import Magazine
from flask import flash

# Read 
@app.route('/dashboard')
def dashboard():
    data ={
        'id': session["user_id"]
    }
    if "user_id" not in session:
        flash("You must be logged in to access dashboard!")
        return redirect('/')
    user = User.get_by_id(data)
    magazines = Magazine.get_all_magazines()
    return render_template('dashboard.html', user=user, magazines=magazines )

@app.route("/show/<int:magazine_id>")
def magazine_detail(magazine_id):
    data ={
        'id': session["user_id"]
    }
    magazine_data = {
        'id': magazine_id
    }
    user=User.get_by_id(data)
    magazine=Magazine.get_by_id(magazine_data)
    return render_template("show.html",user=user, magazine=magazine)

# Create 
@app.route("/create")
def create_magazine_page():
    data ={
        'id': session["user_id"]
    }
    user=User.get_by_id(data)
    return render_template("create.html", user=user)

@app.route("/magazine/create", methods=['POST'])
def create_magazine():
    valid_magazine = Magazine.validate_magazine(request.form)
    if not valid_magazine:
        return redirect('/create')
    Magazine.create_magazine(request.form)
    return redirect('/dashboard')

# Delete 
@app.route("/delete/<int:magazine_id>")
def delete_by_id(magazine_id):
    data = {
        "id": magazine_id
    }
    Magazine.delete_magazine(data)
    return redirect("/dashboard")



