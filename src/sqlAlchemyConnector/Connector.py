from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models.models import *
from src.parsers.ArtistParser import getArtistParser
from src.parsers.PlaylistParser import getPlaylistParser


class Connector:

    def __init__(self):

        dbRoot = 'mysql+pymysql://root@localhost:3306/ci'
        self.__engine = create_engine(dbRoot)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker()
        self.__session.configure(bind=self.__engine)
        self.__dbSession = self.__session()

    # Artist management

    def addArtist(self, stageName, name, lastName, age):
        self.__dbSession.add(Artist(stageName=stageName, name=name, lastName=lastName, age=age))
        self.__dbSession.commit()

    def getArtist(self, stageName):
        return getArtistParser(self.__dbSession.query(Artist).filter_by(stageName=stageName).first())

    def deleteArtist(self,stageName):
        self.__dbSession.delete(self.__dbSession.query(Artist).filter_by(stageName=stageName).first())
        self.__dbSession.commit()

    # Playlist management

    def getPlaylist(self, playlistName):
        return getPlaylistParser(self.__dbSession.query(Playlist).filter_by(playlistName=playlistName).first())

    def addPlaylist(self, playlistName, userName, description):
        self.__dbSession.add(Playlist(playlistName=playlistName, userName=userName, description=description))
        self.__dbSession.commit()

    def deletePlaylist(self, playlistName):
        self.__dbSession.delete(self.__dbSession.query(Playlist).filter_by(playlistName=playlistName).first())
        self.__dbSession.commit()

    # User management

    def addUser(self,userName,password, name, lastName, age):
        newUserData = User_Data(userName=userName, name=name, lastName = lastName, age=age)
        newUserLogin = User_Login(userName=userName, password=password)

        self.__dbSession.add(newUserData)
        self.__dbSession.commit()
        self.__dbSession.add(newUserLogin)
        self.__dbSession.commit()

    def deleteUser(self, userName):

        self.__dbSession.delete(self.__dbSession.query(User_Data).filter_by(userName=userName).first())
        self.__dbSession.commit()
