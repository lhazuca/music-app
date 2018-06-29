from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.models import *
from src.parsers.TrackParse import getTrackLikeNameParser
from src.parsers.TrackParse import getTrackParser
from src.parsers.UserLoginParser import getUserLoginParser
from src.parsers.PlaylistParser import getPlaylistLikeNameParser
from src.parsers.UserParser import getUserParser
from src.parsers.AlbumParser import getAlbumLikeNameParser
from src.parsers.AlbumParser import getAlbumParser
from src.parsers.PlaylistParser import getPlaylistParser

class Connector:

    def __init__(self):
        dbRoot = 'mysql+pymysql://ci:ci@localhost:3306/ci'
        self.__engine = create_engine(dbRoot)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker()
        self.__session.configure(bind=self.__engine)
        self.__dbSession = self.__session()

    # User management

    def addUser(self,userName,password, name, lastName):
        newUserData = User_Data(userName=userName, name=name, lastName=lastName)
        newUserLogin = User_Login(userName=userName, password=password)

        self.__dbSession.add(newUserData)
        self.__dbSession.commit()
        self.__dbSession.add(newUserLogin)
        self.__dbSession.commit()

    def getUser(self, userName):
        user = self.__dbSession.query(User_Data).filter_by(userName=userName).first()
        if user is not None:
            return getUserParser(user)
        else:
            return 'Username not found'

    def getUserLogin(self, userName):
        user = self.__dbSession.query(User_Login).filter_by(userName=userName).first()
        if user is not None:
            return getUserLoginParser(user)
        else:
            return 'Username not found'


    def deleteUser(self, userName):
        user = self.__dbSession.query(User_Data).filter_by(userName=userName).first()
        if user is not None:
            self.__dbSession.delete(user)
            self.__dbSession.commit()
        else:
            'User does not exists'

    def updateUserData(self, userName, userdata):
        self.__dbSession.query(User_Data).filter_by(userName=userName).update(userdata)
        self.__dbSession.commit()

    def updateUserCredentials(self, userName, password):
        self.__dbSession.query(User_Login).filter_by(userName=userName).update(password)
        self.__dbSession.commit()

    # Playlist management

    def getPlaylistLikeName(self, playlistName):
        return getPlaylistLikeNameParser(
                self.__dbSession.query(Playlist).filter(Playlist.playlistName.like("%" + playlistName + "%")).all())

    def addPlaylist(self, playlistName, userName, description):
        newPlaylistData = Playlist(playlistName=playlistName, description=description)
        newPlaylistUserData = PlaylistUser(playlistName=playlistName, userName=userName)
        self.__dbSession.add(newPlaylistData)
        self.__dbSession.commit()
        self.__dbSession.add(newPlaylistUserData)
        self.__dbSession.commit()

    def getPlaylist(self, playlistName):
        return getPlaylistParser(self.__dbSession.query(Playlist).
                                 filter(Playlist.playlistName.__eq__(playlistName)).first())

    def getAllPlaylists(self):
        return getPlaylistLikeNameParser(self.__dbSession.query(Playlist))

    def updatePlaylist(self, playlistName, data):
        self.__dbSession.query(Playlist).filter_by(playlistName=playlistName).update(data)
        self.__dbSession.commit()

    def deletePlaylist(self, playlistName):
        playlistToBeDeleted = self.__dbSession.query(Playlist).filter_by(playlistName=playlistName).first()
        if (playlistToBeDeleted != None):
            self.__dbSession.delete(playlistToBeDeleted)
            self.__dbSession.commit()
            
   #Track methods

    def addTrack(self, owner,trackName, fileContent):
        self.__dbSession.add(Track(trackName=trackName, fileContent=fileContent))
        self.__dbSession.commit()
        self.__dbSession.add(UserTracks(userName=owner,trackName=trackName))
        self.__dbSession.commit()

    def getTrackLikeName(self, trackName):
        return getTrackLikeNameParser(
            self.__dbSession.query(Track).filter(Track.trackName.like("%" + trackName + "%")).all())

    def getTrack(self, trackName):
        track = self.__dbSession.query(Track).filter_by(trackName=trackName).first()
        if track is not None:
            return getTrackParser(track)
        else:
            return 'No id was found'

    def deleteTrack(self, trackId):
        itemToBeDeleted = self.__dbSession.query(Track).filter_by(trackName=trackId).first()
        if itemToBeDeleted is not None:
            self.__dbSession.delete(itemToBeDeleted)
            self.__dbSession.commit()

    def updateTrack(self, trackId, data):
        self.__dbSession.query(Track).filter_by(trackName=trackId).update(data)
        self.__dbSession.commit()

    # Album managment

    def getAlbumLikeName(self,albumName):
        return getAlbumLikeNameParser(self.__dbSession.query(Album).filter(Album.albumName.like("%"+albumName+"%")).all())

    def addAlbum(self, albumName, albumYear, albumOwner):
        newAlbumData = Album(albumName=albumName,albumYear=albumYear)
        newAlbumUserData= AlbumUser(albumName=albumName,userName=albumOwner)
        self.__dbSession.add(newAlbumData)
        self.__dbSession.commit()
        self.__dbSession.add(newAlbumUserData)
        self.__dbSession.commit()

    def deleteAlbum(self, albumName):
        itemToBeDeleted = self.__dbSession.query(Album).filter_by(albumName=albumName).first()
        if (itemToBeDeleted != None):
            self.__dbSession.delete(itemToBeDeleted)
            self.__dbSession.commit()

    def getAlbum(self, albumId):
        return getAlbumParser(self.__dbSession.query(Album).filter(Album.albumName.__eq__(albumId)).first())

    def updateAlbum(self, albumId, data):
        self.__dbSession.query(Album).filter_by(albumName=albumId).update(data)
        self.__dbSession.commit()

