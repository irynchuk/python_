from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model, UserMixin):
    tablename = "user"
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(45), nullable=False, unique=True)
    firstName = db.Column(db.VARCHAR(45), nullable=False)
    lastName = db.Column(db.VARCHAR(45), nullable=False)
    email = db.Column(db.VARCHAR(45), nullable=False)
    password = db.Column(db.VARCHAR(245), nullable=False)
    phone = db.Column(db.VARCHAR(45), nullable=True)
    userStatus = db.Column(db.VARCHAR(45), nullable=True)
    def __init__(self, userId, username, firstName, lastName, email, password, phone, userStatus):
        self.userId = userId
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    def __repr__(self):
        return '{' + f' "userId" : "{self.userId}",' \
                     f' "username" : "{self.username}",' \
                     f' "firstName" : "{self.firstName}",' \
                     f' "lastName" : "{self.lastName}",' \
                     f' "email" : "{self.email}",' \
                     f' "password" : "{self.password}",' \
                     f' "phone" : "{self.phone}",' \
                     f' "userStatus" : "{self.userStatus}",' + '}'\
