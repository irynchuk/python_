from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Member(db.Model, UserMixin):
    tablename = "member"
    memberId = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Integer, nullable=False)
    role = db.Column(db.VARCHAR(45), nullable=False)
    power = db.Column(db.VARCHAR(45), nullable=False)
    def __init__(self, memberId, event, role, power):
        self.memberId = memberId
        self.event = event
        self.role = role
        self.power = power
    def __repr__(self):
        return '{' + f' "memberId" : "{self.memberId}",' \
                     f' "event" : "{self.event}",' \
                     f' "role" : "{self.role}",' \
                     f' "power" : "{self.power}",' + '}'\
