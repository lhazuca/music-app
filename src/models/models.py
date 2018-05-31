from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'Artist'
    stageName = Column(String(40), primary_key=True)
    name = Column(String(30))
    lastName = Column(String(30))
    age = Column(Integer())
