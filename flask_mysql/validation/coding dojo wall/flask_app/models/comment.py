from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Comment:
    db = "the_wall"
    def __init__(self,data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.post_id = data['post_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO comments (content,user_id,post_id) VALUES (%(comment)s,%(user_id)s,%(post_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM comments WHERE comments.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)