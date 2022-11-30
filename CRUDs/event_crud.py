from flask import Flask, request, redirect, abort
from flask_bcrypt import Bcrypt
from flask_expects_json import expects_json
from Models.event import Event
event_schema = {
    "type": "object",
    "properties": {
        "eventId": {"type": "integer"},
        "name": {"type": "string"},
        "dayStart": {"type": "string"},
        "dayEnd": {"type": "string"},
        "timeStart": {"type": "string"},
        "timeEnd": {"type": "string"},
        "status": {"type": "string"},
    },
    "required": ["eventId", "name", "dayStart", "dayEnd", "timeStart", "timeEnd", "status"]
}
event_update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "dayStart": {"type": "string"},
        "dayEnd": {"type": "string"},
        "timeStart": {"type": "string"},
        "timeEnd": {"type": "string"},
        "status": {"type": "string"},
    },
    "required": ["name", "dayStart", "dayEnd", "timeStart", "timeEnd", "status"]
}
def load_event_crud(application, database):
    app = application
    db = database
    bcryptor = Bcrypt(app)
    @app.route('/event', methods=['POST'])  # Create new event
    @expects_json(event_schema)
    def CreateEvent():
        content_type = request.headers.get('Content-Type')
        if request.method == 'POST':
            if content_type == 'application/json':
                json_data = request.get_json()
                new_event = Event(
                    eventId=json_data["eventId"],
                    name=json_data["name"],
                    dayStart=json_data["dayStart"],
                    dayEnd = json_data["dayEnd"],
                    timeStart = json_data["timeStart"],
                    timeEnd = json_data["timeEnd"],
                    status = json_data["status"]
                )
                db.session.add(new_event)
                db.session.commit()
                return "Event successfully added", 200
            else:
                return "Wrong content type supplied, JSON expected", 400
        else:
            return "Wrong request", 400
    @app.route('/event/<int:eventId>')  # Retrieve single event
    def RetrieveSingleEventInfo(eventId):
        event = db.session.query(Event).filter_by(eventId=eventId).first()
        if event:
            return str(event)
        else:
            return "Event not found", 400
    @app.route('/event/<int:eventId>', methods=['PUT'])  # update event
    @expects_json(event_update_schema)
    def UpdateEventInfo(eventId):
        event = db.session.query(Event).filter_by(eventId=eventId).first()
        content_type = request.headers.get('Content-Type')
        if request.method == 'PUT':
            if content_type == 'application/json':
                if event:
                    json_data = request.get_json()
                    event.name = json_data['name']
                    dayStart = json_data["dayStart"],
                    dayEnd = json_data["dayEnd"],
                    user.timeStart = json_data['timeStart']
                    timeEnd = json_data["timeEnd"],
                    status = json_data["status"]
                    db.session.commit()
                    return redirect(f'/event/{eventId}')
                else:
                    return "Event not found", 400
            else:
                return "Wrong content type supplied, JSON expected", 400
        else:
            return "Wrong request", 400
    @app.route('/event/<int:eventId>', methods=['DELETE'])  # delete event
    def DeleteEvent(eventId):
        event = db.session.query(Event).filter_by(eventId=eventId).first()
        if request.method == 'DELETE':
            if event:
                db.session.delete(event)
                db.session.commit()
                return "Event successfully deleted", 200
            else:
                return "Event not found", 400
        else:
            return "Wrong request", 400
    @app.route('/event/<string:name>')
    def RetrieveSingleEventsInfo(name):
        event = db.session.query(Event).filter_by(name=name).first()
        if event:
            return str(event)
        else:
            return "Evemt not found", 400
