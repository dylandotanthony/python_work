from crypt import methods
from flask import Flask, render_template, request, session , redirect
import random

app = Flask(__name__)
app.secret_key = 'yadabobbbaba'

# import the random module
# random number between 1-100



@app.route('/')
def index():
    if "number" not in session:
        session['number'] = random.randint(1, 100)
    return render_template("index.html")


@app.route('/guess', methods = ['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__": 
    app.run(debug=True,port=5001)