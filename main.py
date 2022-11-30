from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import attributes as atr
from flask_cors import CORS
from CRUDs.event_crud import load_event_crud
from CRUDs.member_crud import load_member_crud
from CRUDs.user_crud import load_user_crud
app = Flask(__name__)
conn = ("postgresql+psycopg2://postgres:pass@localhost:5432/iiskovych")
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'test-secret-key'
db = SQLAlchemy(app)
CORS(app)
if __name__ == "__main__":
    load_event_crud(app, db)
    load_member_crud(app, db)
    load_user_crud(app, db)
    app.run(debug=True)
