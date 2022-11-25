from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Post:
    db = "the_wall"
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        

    @classmethod
    def save(cls,data):
        query = "INSERT INTO posts (content,user_id) VALUES (%(content)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM posts WHERE posts.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
