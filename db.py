import psycopg2
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import create_engine, ForeignKey, Text, Enum
from sqlalchemy import Column, Integer, Date, TIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from enum import Enum as enum

engine = create_engine('postgresql+psycopg2://postgres:mypass@localhost:5432/iiskovych')
base = declarative_base()


class Users(base):
    __tablename__ = "users"

    userId = Column(Integer, ForeignKey("userName.userId"), primary_key=True)
    username = Column(VARCHAR(45), nullable=False)
    firstName = Column(VARCHAR(45), nullable=False)
    lastName = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)
    password = Column(VARCHAR(45), nullable=False)
    phone = Column(VARCHAR(45), nullable=True)
    userStatus = Column(VARCHAR(45), nullable=True)

    def __init__(self, userId, username, firstName, lastName, email, password, phone, userStatus):
        self.userId = userId
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus


class UserName(base):
    __tablename__ = "userName"
    userId = Column(Integer, primary_key=True)
    firstName = Column(VARCHAR(45), nullable=False)
    lastName = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)

    def __init__(self, userId, firstName, lastName, email):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email


class Member(base):
    __tablename__ = "member"
    memberId = Column(Integer, ForeignKey("userName.userId"), primary_key=True)
    event = Column(Integer, ForeignKey("event.eventId"), nullable=False)
    role = Column(VARCHAR(45), nullable=False)
    power = Column(VARCHAR(45), nullable=False)

    def __init__(self, memberId, event, role, power):
        self.memberId = memberId
        self.event = event
        self.role = role
        self.power = power


class Event(base):
    __tablename__ = "event"
    eventId = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45),  nullable=False)
    dayStart = Column(Date,  nullable=False)
    dayEnd = Column(Date,  nullable=False)
    timeStart = Column(TIME,  nullable=False)
    timeEnd = Column(TIME,  nullable=False)
    status = Column(VARCHAR(45), nullable=False)

    def __init__(self, eventId, name, dayStart, dayEnd, timeStart, timeEnd, status):
        self.eventId = eventId
        self.name = name
        self.dayStart = dayStart
        self.dayEnd = dayEnd
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.status = status

# base.metadata.tables["users"].create(bind=engine)


base.metadata.create_all(engine)