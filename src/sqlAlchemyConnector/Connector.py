from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models.models import *
from src.parsers.ArtistParser import getArtistParser

class Connector:

    def __init__(self):

        dbRoot = 'mysql+pymysql://root@localhost:3306/ci'
        self.__engine = create_engine(dbRoot)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker()
        self.__session.configure(bind=self.__engine)
        self.__dbSession = self.__session()

    def addArtist(self, stageName, name, lastName, age):
        self.__dbSession.add(Artist(stageName=stageName, name=name, lastName=lastName, age=age))
        self.__dbSession.commit()

    def getArtist(self, stageName):
        return getArtistParser(self.__dbSession.query(Artist).filter_by(stageName=stageName).first())

    def deleteArtist(self,stageName):
        self.__dbSession.delete(self.__dbSession.query(Artist).filter_by(stageName=stageName).first())
        self.__dbSession.commit()