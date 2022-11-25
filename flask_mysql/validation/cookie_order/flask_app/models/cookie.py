from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Cookie:
    db = "cookies"
    def __init__(self,data):
        self.id = data['id']
        self.customer_name = data['customer_name'] 
        self.cookie_type = data['cookie_type']
        self.num_box = data['num_box']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie;"
        result = connectToMySQL(cls.db).query_db(query)
        cookies = []
        for c in result:
            cookies.append(cls(c))
        return cookies

    @classmethod
    def save(cls,data):
        query = "INSERT INTO cookie (customer_name, cookie_type, num_box, created_at, updated_at) VALUES (%(customer_name)s, %(cookie_type)s, %(num_box)s, NOW(), NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cookie WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE cookie SET customer_name=%(customer_name)s, cookie_type=%(cookie_type)s, num_box=%(num_box)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_order(cookie):
        is_valid = True # we assume this is true
        if len(cookie['customer_name']) < 2:
            flash("Customer name must be at least 2 characters.")
            is_valid = False
        if len(cookie['cookie_type']) < 3:
            flash("Cookie Type must be at least 2 characters.")
            is_valid = False
        if int(cookie['num_box']) < 0:
            flash("Number of Boxes must be at least 1.")
            is_valid = False
        return is_valid


