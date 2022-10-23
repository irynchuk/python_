import db
from db import Users, UserName, Member, Event
from  sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)

session = Session()

#user = Users(14, 'Irynchuk', 'Ira', 'Iskovych', 'iryna.iskovych.kn.2021@lpnu.ua', 'pass','0937607986', 'active')
#name = UserName(14, 'Ira', 'Iskovych', 'iryna.iskovych.kn.2021@lpnu.ua')
#event = Event(1, 'New Year', '31/12/2022', '1/1/2023', '15:00', '16:00', 'future')
member = Member(14, 1, 'admin', 'edit')


#session.add(user)
#session.add(name)
#session.add(event)
session.add(member)

session.commit()