from flask import Flask, render_template
app = Flask(__name__)

# http://localhost:5001 - should display 8 by 8 checkerboard
@app.route('/')
def ck_one():
    return render_template("index.html",row=8, column=8, color1='red', color2='black')

# http://localhost:5001/4 - should display 8 by 4 checkerboard
@app.route('/4')
def ck_two():
    return render_template("index.html",row=8, column=4, color1='red', color2='black')

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.
@app.route('/<int:row>/<int:column>')
def ck_three(row,column):
    return render_template("index.html",row=row, column=column, color1='red', color2='black')

#SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") 
# and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:row>/<int:column>/<string:color1>/<string:color2>')
def ck_four(row,column,color1,color2):
    return render_template("index.html",row=row, column=column, color1=color1, color2=color2)



if __name__=="__main__": 
    app.run(debug=True,port=5001)



