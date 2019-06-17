from src.database import Database
from flask import session
import uuid

class User(object):
    def __init__(self, email, password, _id = None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        print(data)
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            #check the password
            return user.password == password
        return False

    @staticmethod
    def register(email, password):
        user = User.get_by_email(email)
        if user is None:
            #If the user doesn't exit
            user = User(email, password)
            user.save_to_mongo()
            session['email'] = email
            return True
        else:
            #User exists
            return False

    @staticmethod
    def login(user_email):
        #login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        pass

    def json(self):
        return {
            'email': self.email,
            'password': self.password, #this is not safe because it's not encrypted
            '_id': self._id
        }

    def save_to_mongo(self):
        Database.insert('users', self.json())

