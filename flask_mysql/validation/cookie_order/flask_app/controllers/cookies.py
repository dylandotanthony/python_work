from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.cookie import Cookie

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookies():
    return render_template("index.html", cookies=Cookie.get_all())

@app.route('/cookies/new')
def new():
    return render_template("order.html")

@app.route('/cookies/create', methods=['POST'])
def create_order():
    if not Cookie.validate_order(request.form):
        return redirect('/cookies/new')
    print(request.form)
    Cookie.save(request.form)
    return redirect('/')

@app.route('/cookie/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("update_order.html", cookie=Cookie.get_one(data))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not Cookie.validate_order(request.form):
        return redirect(f'/cookie/edit/{id}')
    data = {
        'id':id,
        "customer_name":request.form['customer_name'],
        "cookie_type": request.form['cookie_type'],
        "num_box": request.form['num_box'],
    }
    Cookie.update(data)
    return redirect('/')
