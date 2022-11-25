from flask import Flask 
app = Flask(__name__)


# Create a root route ("/") that responds with "Hello World!"
# localhost:5000/ - have it say "Hello World!"

@app.route('/')
def hello_world(): 
    return 'Hello World'



# Create a route that responds with "Dojo!"
# localhost:5000/dojo - have it say "Dojo!"

@app.route('/Dojo')
def dojo(): 
    return 'Dojo!'


# Create a route that responds with "Hi" and whatever name is in the URL after /say/
# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"

@app.route('/say/<name>')
def sayhi(name):
    return "Hi " + name + "!"


# Create a route that responds with the given word repeated as many times as specified in the URL
# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times

@app.route('/repeat/<string:object>/<int:num>')
def hello(object,num):
    return f"{object * num}"

# NINJA BONUS: Ensure the names provided in the 3rd task are strings



# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string



# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, 
# they receive an error message saying "Sorry! No response. Try again."

if __name__=="__main__": 
    app.run(debug=True,port=5001)