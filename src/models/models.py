from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'Artist'
    stageName = Column(String(40), primary_key=True)
    name = Column(String(30))
    lastName = Column(String(30))
    age = Column(Integer())

class Playlist(Base):
    __tablename__ = 'Playlist'
    playlistName = Column(String(50), primary_key=True)
    userName = Column(String(40), ForeignKey('User_Data.userName', ondelete='CASCADE'), primary_key=True)
    description = Column(String(100))

class User_Data(Base):
    __tablename__ = 'User_Data'
    userName = Column(String(50), primary_key=True)
    name = Column(String(40))
    lastName = Column(String(40))
    age = Column(Integer())

class User_Login(Base):
    __tablename__ = 'User_Login'
    userName = Column(String(50), ForeignKey('User_Data.userName',ondelete='CASCADE'),primary_key=True)
    password = Column(String(128))
    lastPassChange = Column(DateTime, default=func.now())
