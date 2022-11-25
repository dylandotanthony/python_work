from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
bcrypt = Bcrypt(app)

class Band:
    db = "band"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name'] 
        self.genre = data['genre']
        self.city = data['city']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
        self.on_data =[]

# Create
    # @classmethod
    # def create_band(cls,data):
    #     if not cls.validate_band(data):
    #         return False
    #     query = """INSERT INTO bands (name, genre, city, user_id) 
    #     VALUES (%(name)s, %(genre)s, %(city)s, %(user_id)s);"""
    #     results = connectToMySQL(db).query_db(query,data)
    #     band = cls.get_by_id(results)
    #     return band

    @classmethod
    def create_band(cls,data):
        query = """INSERT INTO bands (name, genre, city, user_id)  
        VALUES (%(name)s, %(genre)s, %(city)s, %(user_id)s);"""
        return connectToMySQL(cls.db).query_db(query,data)







# Read
    # @classmethod
    # def get_bands(cls):
    #     query = "SELECT * FROM bands LEFT JOIN users ON user_id = users.id ;"
    #     results = connectToMySQL(cls.db).query_db(query)
    #     bands =[]
    #     for row in results:
    #         band = cls(row)
    #         user_data = {
    #             'id': row['users.id'],
    #             'first_name' : row['first_name'],
    #             'last_name' : row['last_name'],
    #             'email' : row['email'],
    #             'password' : row['password'],
    #             'created_at' : row['users.created_at'],
    #             'updated_at' : row['users.updated_at']
    #         }
    #         band.user = user.User(user_data)
    #         bands.append(band)
        # return bands


    # @classmethod
    # def get_all_bands(cls):
    #     query =  """SELECT bands.id, bands.created_at, bands.updated_at, city, genre, name,
    #     users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
    #     FROM bands
    #     JOIN users on users.id = bands.user_id;"""
    #     band_data = connectToMySQL(cls.db).query_db(query)
    #     bands = []
    #     for band in band_data:
    #         band_obj = cls(band)
    #         band_obj.user = user.User(
    #             {
    #                 "id":band["user_id"],
    #                 "first_name": band["first_name"],
    #                 "last_name": band["last_name"],
    #                 "email": band["email"],
    #                 "created_at": band["uc"],
    #                 "updated_at":band["uu"]
    #             }
    #         )
    #         bands.append(band_obj)
    #     return bands

    @classmethod
    def get_all_bands(cls):
        query = "SELECT * FROM bands LEFT JOIN users ON user_id = users.id ;"
        results = connectToMySQL(cls.db).query_db(query)
        bands =[]
        for row in results:
            band = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            band.user = user.User(user_data)
            bands.append(band)
        return bands

    @classmethod
    def get_all_bands_with_user(cls,data):
        query = "SELECT * FROM bands LEFT JOIN users ON user_id = users.id WHERE bands.user_id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        bands =[]
        for row in results:
            band = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            band.user = user.User(user_data)
            bands.append(band)
        return bands






    @classmethod
    def get_by_band(cls,data):
        query = """SELECT * FROM users LEFT JOIN bands 
        ON users.id = bands.user_id WHERE users.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        bands = []
        if len(results) == 0:
            return None
        else:
            if results[0]['title'] != None:
                for row in results:
                    a_user = user.User(row)
                    mag_data = {
                        "id" : row['bands.id'],
                        'name' : row['name'],
                        'genre' : row['genre'],
                        'city' : row['city'],
                        'created_at' : row['bands.created_at'],
                        'updated_at' : row['bands.updated_at'],
                        'user_id': row['user_id']
                    }
                    band_ob =cls(mag_data)
                    band_ob.user = a_user
                    bands.append(band_ob)
        return bands



    # @classmethod
    # def get_all_bands_with_user(cls,data):
    #     query = "SELECT * FROM bands LEFT JOIN users ON user_id = users.id WHERE bands.user_id=%(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     bands =[]
    #     for row in results:
    #         band = cls(row)
    #         user_data = {
    #             'id': row['users.id'],
    #             'first_name' : row['first_name'],
    #             'last_name' : row['last_name'],
    #             'email' : row['email'],
    #             'password' : row['password'],
    #             'created_at' : row['users.created_at'],
    #             'updated_at' : row['users.updated_at']
    #         }
    #         band.user = user.User(user_data)
    #         bands.append(band)
    #     return bands

    # @classmethod
    # def get_by_id(cls, band_id):
    #     data = {"id": band_id}
    #     query = "SELECT * FROM bands WHERE id = %(id)s;"
    #     results = connectToMySQL(db).query_db(query,data)[0]
    #     user_obj = user.User.get_by_id(results)
    #     band.user = user_obj
    #     return band

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM bands WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        band = cls(row)
        return band
#Update
    @classmethod
    def update_band(cls,data,session_id):
        band = cls.get_by_id(data['id'])
        if band.user.id != session_id:
            flash("You must be the creator to update this band!")
            return False
        if not cls.validate_band(data): 
            return False
        query = """UPDATE bands
        SET name = %(name)s, genre = %(genre)s, city = %(city)s
        WHERE id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query,data)
        band = cls.get_by_id(result["id"])
        return band

# Delete 
    # @classmethod
    # def delete_band(cls, band_id):
    #     data = {"id": band_id}
    #     query = "DELETE FROM bands WHERE id = %(id)s;"
    #     connectToMySQL(cls.db).query_db(query,data)
    #     return band_id

    @classmethod
    def delete_band(cls, data):
        query = "DELETE FROM bands WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    

# Validate
    # @staticmethod
    # def validate_band(band_data):
    #     is_valid = True 
    #     flash_string = " field is required and must be atleast 2 characters"
    #     if len(band_data['name']) < 2:
    #         flash("Band Name" + flash_string )
    #         is_valid = False
    #     if len(band_data['genre']) < 2:
    #         flash("Music Genre" + flash_string )
    #         is_valid = False
    #     if len(band_data['city']) < 2:
    #         flash("Home City" + flash_string)
    #         is_valid = False
    #     if "name" not in band_data:
    #         flash("Band name is REQUIRED!")
    #         is_valid = False
    #     if "genre" not in band_data:
    #         flash("Music Genre is REQUIRED!")
    #         is_valid = False
    #     if "city" not in band_data:
    #         flash("Home City is REQUIRED!" )
    #         is_valid = False
    #     return is_valid  

    @staticmethod
    def validate_band(band):
        flash_string = " field is required and must be atleast 2 characters"
        is_valid = True 
        if len(band['name']) < 2:
            flash("Band Name" + flash_string )
            is_valid = False
        if len(band['genre']) < 2:
            flash("Band Name" + flash_string)
        if len(band['city']) < 2:
            flash("Band Name" + flash_string)
            is_valid = False
        if "name" not in band:
            flash("Band name is REQUIRED!")
            is_valid = False
        if "genre" not in band:
            flash("Music Genre is REQUIRED!")
            is_valid = False
        if "city" not in band:
            flash("Home City is REQUIRED!" )
            is_valid = False
        return is_valid