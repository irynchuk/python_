from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Event(db.Model, UserMixin):
    tablename = "event"
    eventId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(45),  nullable=False)
    dayStart = db.Column(db.VARCHAR(45),  nullable=False)
    dayEnd = db.Column(db.VARCHAR(45),  nullable=False)
    timeStart = db.Column(db.VARCHAR(45),  nullable=False)
    timeEnd = db.Column(db.VARCHAR(45),  nullable=False)
    status = db.Column(db.VARCHAR(45), nullable=False)
    def __init__(self, eventId, name, dayStart, dayEnd, timeStart, timeEnd, status):
        self.eventId = eventId
        self.name = name
        self.dayStart = dayStart
        self.dayEnd = dayEnd
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.status = status
    def __repr__(self):
        return '{' + f' "eventId" : "{self.eventId}",' \
                     f' "name" : "{self.name}",' \
                     f' "dayStart" : "{self.dayStart}",' \
                     f' "dayEnd" : "{self.dayEnd}",' \
                     f' "timeStart" : "{self.timeStart}",' \
                     f' "timeEnd" : "{self.timeEnd}",' \
                     f' "status" : "{self.status}",' + '}'\
