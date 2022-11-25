from flask import Flask, render_template
app = Flask(__name__)


#Have the /play route render a template with 3 blue boxes
@app.route('/play')
def play():
    return render_template("index.html",num=3, color="lightblue")

# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:num>')
def play_one(num):
    return render_template('index.html', num=num, color="lightblue")


#Have the /play/<x>/<color> route render a template with
#  x number of boxes the color of the provided value
@app.route('/play/<int:num>/<string:color>')
def play_two(num,color):
    return render_template('index.html', num=num, color=color)


if __name__=="__main__": 
    app.run(debug=True,port=5001)