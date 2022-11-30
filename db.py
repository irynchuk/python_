import psycopg2
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import create_engine, ForeignKey, Text, Enum
from sqlalchemy import Column, Integer, Date, TIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from marshmallow import Schema, fields, validate

engine = create_engine('postgresql+psycopg2://postgres:pass@localhost:5432/iiskovych')

base = declarative_base()


class User(base):
    tablename = "user"
    userId = Column(Integer, ForeignKey("userName.userId"), primary_key=True)
    username = Column(VARCHAR(45), nullable=False)
    firstName = Column(VARCHAR(45), nullable=False)
    lastName = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)
    password = Column(VARCHAR(45), nullable=False)
    phone = Column(Integer, nullable=True)
    userType = Column(VARCHAR(45), nullable=False)

    def init(self, userId, username, firstName, lastName, email, password, phone, userType):
        self.userId = userId
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userType = userType


class UserName(base):
    tablename = "userName"
    userId = Column(Integer, primary_key=True)
    firstName = Column(VARCHAR(45), nullable=False)
    lastName = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)
    userType = Column(VARCHAR(45), nullable=False)

    def init(self, userId, firstName, lastName, email, userType):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userType = userType


class Car(base):
    tablename = "car"
    carId = Column(Integer, primary_key=True)
    model = Column(VARCHAR(45), nullable=False)
    carType = Column(VARCHAR(45), nullable=False)
    petrol = Column(VARCHAR(45), nullable=False)
    carStatus = Column(VARCHAR(45), nullable=False)

    def init(self, carId, model, carType, petrol, carStatus):
        self.carId = carId
        self.model = model
        self.carType = carType
        self.petrol = petrol
        self.carStatus = carStatus


class RentSeance(base):
    tablename = "RentSeance"
    rentId = Column(Integer, primary_key=True)
    rentStart = Column(Date, nullable=False)
    timeStart = Column(Time, nullable=False)
    rentEnd = Column(Date, nullable=False)
    timeEnd = Column(Time, nullable=False)
    renterId = Column(Integer, ForeignKey(User.userId), nullable=False)
    carId = Column(Integer, ForeignKey(Car.carId), nullable=False)
    status = Column(VARCHAR(45), nullable=False)

    def init(self, rentId, rentStart, timeStart, rentEnd, timeEnd, renterId, carId, status):
        self.rentId = rentId
        self.rentStart = rentStart
        self.timeStart = timeStart
        self.rentEnd = rentEnd
        self.timeEnd = timeEnd
        self.renterId = renterId
        self.carId = carId
        self.status = status


base.metadata.create_all(engine)
