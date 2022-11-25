from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'yeetyyeet5454'

@app.route('/')
def index():
    if "counter" not in session: 
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/add')
def add_two():
    session['counter'] += 1
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


# @app.route('/destroy_session')


if __name__=="__main__": 
    app.run(debug=True,port=5001)