from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    # users = User.get_all()
    # print(users)
    return render_template("index.html", users=User.get_all())

@app.route('/user/new')
def new():

    return render_template("create.html")
    

@app.route('/user/create', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        # redirect to the route where the user form is rendered.
        return redirect('/user/new')
    print(request.form)   
    User.save(request.form)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html", user=User.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/term/<int:id>')
def term(id):
    data ={
        "id":id
    }
    User.term(data)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show.html", user=User.get_one(data))

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')

    # flash("Email cannot be blank!", 'email')