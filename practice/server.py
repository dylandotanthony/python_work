from flask import Flask, render_template, request, session , redirect
app = Flask(__name__)

app.secret_key = 'YAHOOOOO'

@app.route('/')


if __name__=="__main__": 
    app.run(debug=True,port=5001)