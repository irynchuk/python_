import db
from db import Users, UserName, Member, Event
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)

session = Session()

user1 = Users('Irynchuk', 'Ira', 'Iskovych', 'iryna.iskovych.kn.2021@lpnu.ua', 'pass','0937607986', 'active')
name1 = UserName('Ira', 'Iskovych', 'iryna.iskovych.kn.2021@lpnu.ua')
user2 = Users('Kida', 'Lida', 'Kovtynenko', 'kida@gmail.com', 'arty', '0456537986', 'active')
name2 = UserName('Kida', 'Kovtynenko', 'kida@gmail.com')
event1 = Event('New Year', '31/12/2022', '1/1/2023', '15:00', '16:00', 'future')

session.add(user1)
session.add(name1)
session.add(user2)
session.add(name2)
session.add(event1)

session.commit()

member1 = Member(1, 'admin', 'edit')
member2 = Member(1, 'admin', 'edit')

session.add(member1)
session.add(member2)

session.commit()
