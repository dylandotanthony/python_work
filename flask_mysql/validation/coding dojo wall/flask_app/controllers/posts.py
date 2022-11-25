from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.comment import Comment
from flask_app.models.post import Post


@app.route('/post', methods=['POST'])
def post():
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        "user_id": request.form['user_id'],
        "content": request.form['user_id']
    }
    Post.save(data)
    return redirect('/wall')