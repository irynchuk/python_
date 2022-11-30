from flask import Flask, request, redirect, abort
from flask_bcrypt import Bcrypt
from flask_expects_json import expects_json
from Models.user import User
user_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "phone": {"type": "string"},
        "userStatus": {"type": "string"}
    },
    "required": ["userId", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"]
}
user_update_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "phone": {"type": "string"},
        "userStatus": {"type": "string"}
    },
    "required": ["username", "firstName", "lastName", "email", "password", "phone", "userStatus"]
}
def load_user_crud(application, database):
    app = application
    db = database
    bcryptor = Bcrypt(app)
    @app.route('/user', methods=['POST'])
    @expects_json(user_schema)
    def CreateUser():
        content_type=request.headers.get('Content-Type')
        if content_type == 'application/json':
            json_data = request.get_json()
            hashed_password = bcryptor.generate_password_hash(json_data['password'])
            new_user = User(userId=json_data["userId"],
                            username=json_data["username"],
                            firstName=json_data["firstName"],
                            lastName=json_data["lastName"],
                            email=json_data["email"],
                            password=hashed_password,
                            phone=json_data["phone"],
                            userStatus=json_data["userStatus"])
            db.session.add(new_user)
            db.session.commit()
            return "Registration successful", 200
        else:
            return 'Content-Type not supported!', 400
    @app.route('/user/<int:userId>')  # Retrieve single user
    def RetrieveSingleUserInfo(userId):
        user = db.session.query(User).filter_by(userId=userId).first()
        if user:
            return str(user)
        else:
            return "User not found", 400
    @app.route('/user/<int:userId>', methods=['PUT'])  # update user
    @expects_json(user_update_schema)
    def UpdateUserInfo(userId):
        user = db.session.query(User).filter_by(userId=userId).first()
        content_type = request.headers.get('Content-Type')
        if request.method == 'PUT':
            if content_type == 'application/json':
                if user:
                    json_data = request.get_json()
                    hashed_password = bcryptor.generate_password_hash(json_data['password'])
                    user.username = json_data['username']
                    firstName = json_data["firstName"],
                    lastName = json_data["lastName"],
                    user.email = json_data['email']
                    user.password = hashed_password
                    phone = json_data["phone"],
                    userStatus = json_data["userStatus"]
                    db.session.commit()
                    return redirect(f'/user/{userId}')
                else:
                    return "User not found", 400
            else:
                return "Wrong content type supplied, JSON expected", 400
        else:
            return "Wrong request", 400
    @app.route('/user/<int:userId>', methods=['DELETE'])  # delete user
    def DeleteUser(userId):
        user = db.session.query(User).filter_by(userId=userId).first()
        if request.method == 'DELETE':
            if user:
                db.session.delete(user)
                db.session.commit()
                return "User successfully deleted", 200
            else:
                return "User not found", 400
        else:
            return "Wrong request", 400

    @app.route('/user/<string:username>')
    def RetrieveSingleUsersInfo(username):
        user = db.session.query(User).filter_by(username=username).first()
        if user:
            return str(user)
        else:
            return "User not found", 400
