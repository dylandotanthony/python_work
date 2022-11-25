from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

class Magazine:
    db = "magazine"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        self.on_mag =[]

# Create
    @classmethod
    def create_magazine(cls,data):
        query = """INSERT INTO magazines (title, description, user_id) 
        VALUES (%(title)s, %(description)s, %(user_id)s);"""
        return connectToMySQL(cls.db).query_db(query,data)

# Read
    @classmethod
    def get_all_magazines(cls):
        query = "SELECT * FROM magazines LEFT JOIN users ON user_id = users.id ;"
        results = connectToMySQL(cls.db).query_db(query)
        magazines =[]
        for row in results:
            magazine = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            magazine.user = User(user_data)
            magazines.append(magazine)
        return magazines

    @classmethod
    def get_by_magazine(cls,data):
        query = """SELECT * FROM users LEFT JOIN magazines 
        ON users.id = magazines.user_id WHERE users.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        magazines = cls( results[0] )
        if len(results) == 0:
            return None
        else:
            mag_creator = user.User(results[0])
            if results[0]['title'] != None:
                for row in results:
                    # magazine = cls(row)
                    mag_data = {
                        "id" : row['id'],
                        'title' : row['title'],
                        'description' : row['description'],
                        'created_at' : row['created_at'],
                        'updated_at' : row['updated_at'],
                    }
                    mag_ob =cls(mag_data)
                    # magazine.user = user.User(user_data)
                    magazines.on_mag.append(user.User(mag_ob))
        # return mag_creator
        #             mag_obj = cls(mag_data)
        #             mag_creator.magazines.append(mag_obj)
        return mag_creator


    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM magazines WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        magazine = cls(row)
        return magazine

    # @classmethod
    # def get_by_magazine(cls,udata):
    #     query = """SELECT * FROM users LEFT JOIN magazines 
    #     ON users.id = magazines.user_id WHERE users.id = %(id)s;"""
    #     results = connectToMySQL(cls.db).query_db(query,udata)
    #     if len(results) == 0:
    #         return None
    #     else:
    #         mag_creator = User(results[0])
    #         if results[0]['title'] != None:
    #             for user_mag_data in results:
    #                 mag_data = {
    #                     "id" : user_mag_data['id'],
    #                     'title' : user_mag_data['title'],
    #                     'description' : user_mag_data['description'],
    #                     'created_at' : user_mag_data['created_at'],
    #                     'updated_at' : user_mag_data['updated_at'],
    #                 }
    #                 mag_obj = cls(mag_data)
    #                 mag_creator.magazines.append(mag_obj)
    #     return mag_obj
        # magazines =[]
        # for row in results:
        #     magazine = cls(row)
        #     user_data = {
        #         'id': row['users.id'],
        #         'first_name' : row['first_name'],
        #         'last_name' : row['last_name'],
        #         'email' : row['email'],
        #         'password' : row['password'],
        #         'created_at' : row['users.created_at'],
        #         'updated_at' : row['users.updated_at']
        #     }
        #     magazine.user = User(user_data)
        #     magazines.append(magazine)
        # return magazines



# Update
    @classmethod
    def update_magazine(cls,data,session_id):
        magazine = cls.get_by_id(data['id'])
        if magazine.user.id != session_id:
            flash("You must be the creator to update this magazine!")
            return False
        if not cls.validate_magazine(data): 
            return False
        query = """UPDATE magazines
        SET title=%(title)s, description=%(description)s
        WHERE id =%(id)s;"""
        result = connectToMySQL(cls.db).query_db(query,data)
        magazine = cls.get_by_id(result["id"])
        return magazine

# delete 
    @classmethod
    def delete_magazine(cls, data):
        query = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

# Validate

    @staticmethod
    def validate_magazine(magazine):
        is_valid = True 
        if len(magazine['title']) < 2:
            flash("Title must be atleast 2 characters! ", "magazine" )
            is_valid = False
        if len(magazine['description']) < 10:
            flash("description must be atleast 10 characters! ", "magazine"  )
            is_valid = False
        return is_valid