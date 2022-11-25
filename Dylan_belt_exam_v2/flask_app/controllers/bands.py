from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models import user
from flask_app.models import band
from flask import flash

# Dashboard
@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        flash("You must be logged in to access dashboard!")
        return redirect('/')

    data ={
        'id': session["user_id"]
    }
    a_user = user.User.get_by_id(data)
    a_bands = band.Band.get_all_bands()
    return render_template('dashboard.html', a_user=a_user, a_bands=a_bands )

# Create
#  
# @app.route("/create")
# def create_band_page():
#     return render_template("create.html")

@app.route("/create")
def create_band_page():
    data ={
        'id': session["user_id"]
    }
    a_user= user.User.get_by_id(data)
    return render_template("create.html", a_user=a_user)



@app.route("/band/create", methods=['POST'])
def create_the_band():
    valid_band = band.Band.validate_band(request.form)    
    if not valid_band:
        return redirect('/create')
    band.Band.create_band(request.form)
    return redirect('/dashboard')

# def register():
#     if not band.Band.validate_band(request.form):
#         return redirect('/create')
#     data = {
#         "name": request.form['name'],
#         "genre": request.form['genre'],
#         "city": request.form['city'],
#         }
#     band.Band.create_band(request.form)
#     a_user = user.User.create_user(data)
#     # store user id into session
#     session['user_id'] = a_user
#     flash('Registration Successful!', "register")
#     return redirect('/dashboard')

# @app.route("/band/create", methods=['POST'])
# def create_band():
#     valid_band = Band.validate_band(request.form)
#     if not valid_band:
#         return redirect('/create')
#     Band.create_band(request.form)
#     return redirect('/dashboard')





# READ 
# @app.route("/show/<int:band_id>")
# def band_detail(band_id):
#     user = User.get_by_id(session["user_id"])
#     band = Band.get_by_id(band_id)
#     return render_template("show.html",user=user, band=band)


# @app.route("/show/<int:user_id>")
# def band_detail(bands_id):
#     data ={
#         'id': session["user_id"]
#     }
#     band_data = {
#         'id': bands_id
#     }
#     a_user= user.User.get_by_id(data)
#     a_band= band.Band.get_by_id(band_data)
#     return render_template("show.html",a_user=a_user, a_band=a_band)





# UPDATE
# @app.route("/edit/<int:band_id>")
# def edit_page(band_id):
#     a_band = band.Band.get_by_id(band_id)
#     return render_template("edit.html", a_band=a_band)


@app.route("/edit/<int:band_id>")
def edit_page(band_id):
    data = {
        "id": band_id
    }
    user_data ={
        'id': session["user_id"]
    }
    a_user= user.User.get_by_id(user_data)
    a_bands = band.Band.get_by_id(data)
    return render_template("edit.html", a_bands=a_bands, a_user=a_user)



@app.route("/update", methods=['POST'])
def edit_band():
    band.Band.update_band(request.form) 
    # if not valid_band:
    #     return redirect(f'/edit/{a_band_id}')
    return redirect('/dashboard')

# Delete
# @app.route("/delete/<int:band_id>")
# def delete_by_id(band_id):
#     Band.delete_band(band_id)
#     return redirect("/dashboard")

@app.route("/delete/<int:bands_id>")
def delete_by_id(bands_id):
    data = {
        "id": bands_id
    }
    band.Band.delete_band(data)
    return redirect("/dashboard")