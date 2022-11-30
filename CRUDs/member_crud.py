from flask import Flask, request, redirect, abort
from flask_bcrypt import Bcrypt
from flask_expects_json import expects_json
from Models.member import Member
member_schema = {
    "type": "object",
    "properties": {
        "memberId": {"type": "integer"},
        "event": {"type": "integer"},
        "role": {"type": "string"},
        "power": {"type": "string"},
    },
    "required": ["memberId", "event", "role", "power"]
}
member_update_schema = {
    "type": "object",
    "properties": {
        "event": {"type": "integer"},
        "role": {"type": "string"},
        "power": {"type": "string"},
    },
    "required": [ "event", "role", "power"]
}
def load_member_crud(application, database):
    app = application
    db = database
    bcryptor = Bcrypt(app)
    @app.route('/member', methods=['POST'])  # Create new member
    @expects_json(member_schema)
    def CreateMemner():
        content_type = request.headers.get('Content-Type')
        if request.method == 'POST':
            if content_type == 'application/json':
                json_data = request.get_json()
                new_member = Member(
                    memberId=json_data["memberId"],
                    event=json_data["event"],
                    role=json_data["role"],
                    power = json_data["power"]
                )
                db.session.add(new_member)
                db.session.commit()
                return "Member successfully added", 200
            else:
                return "Wrong content type supplied, JSON expected", 400
        else:
            return "Wrong request", 400
    @app.route('/member/<int:memberId>')  # Retrieve single member
    def RetrieveSingleMemberInfo(memberId):
        member = db.session.query(Member).filter_by(memberId=memberId).first()
        if member:
            return str(member)
        else:
            return "Member not found", 400
    @app.route('/member/<int:memberId>', methods=['PUT'])  # update member
    @expects_json(member_update_schema)
    def UpdateMemberInfo(memberId):
        member = db.session.query(Member).filter_by(memberId=memberId).first()
        content_type = request.headers.get('Content-Type')
        if request.method == 'PUT':
            if content_type == 'application/json':
                if member:
                    json_data = request.get_json()
                    event = json_data["event"],
                    role = json_data["role"],
                    power = json_data["power"]
                    db.session.commit()
                    return redirect(f'/member/{memberId}')
                else:
                    return "Member not found", 400
            else:
                return "Wrong content type supplied, JSON expected", 400
        else:
            return "Wrong request", 400
    @app.route('/member/<int:memberId>', methods=['DELETE'])  # delete member
    def DeleteMember(memberId):
        member = db.session.query(Member).filter_by(memberId=memberId).first()
        if request.method == 'DELETE':
            if member:
                db.session.delete(member)
                db.session.commit()
                return "Member successfully deleted", 200
            else:
                return "Member not found", 400
        else:
            return "Wrong request", 400
    @app.route('/member/<string:role>')
    def RetrieveSingleMembersInfo(role):
        member = db.session.query(Member).filter_by(role=role).all()
        if member:
            return str(member)
        else:
            return "Member not found", 400
    @app.route('/memberevent/<string:event>')
    def RetrieveSingleMemberEventInfo(event):
        member = db.session.query(Member).filter_by(event=event).all()
        if member:
            return str(member)
        else:
            return "Member not found", 400
