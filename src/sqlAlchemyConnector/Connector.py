from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.models import *
from src.parsers.AlbumParser import getAlbumLikeNameParser
from src.parsers.ArtistParser import getArtistParser
from src.parsers.TrackParse import getTrackLikeNameParser
from src.parsers.TrackParse import getTrackParser
from src.parsers.PlaylistParser import getPlaylistParser
from src.parsers.PlaylistParser import getPlaylistWithSubString
from src.parsers.UserParse import getUserParse


class Connector:

    def __init__(self):
        dbRoot = 'mysql+pymysql://root@localhost:3306/ci'
        self.__engine = create_engine(dbRoot)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker()
        self.__session.configure(bind=self.__engine)
        self.__dbSession = self.__session()

    # Artist management

    def addArtist(self, stageName, name, lastName):
        self.__dbSession.add(User_Data(userName=stageName, name=name, lastName=lastName))
        self.__dbSession.commit()

    def getArtist(self, stageName):
        return getArtistParser(self.__dbSession.query(Artist).filter_by(stageName=stageName).first())

    def deleteArtist(self, stageName):
        first = self.__dbSession.query(User_Data).filter_by(userName=stageName).first()
        if (first != None):
            self.__dbSession.delete(first)
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

    def addPlaylistAudioFile(self, audioFile, playlistName):
        self.__dbSession.add(AudioFileByPlaylist(playlistName=playlistName, audioFile=audioFile))
        self.__dbSession.commit()

    # Artist Audio File management

    def addArtistAudioFile(self, fileName, fileContent, artist):
        self.__dbSession.add(Track(trackName=fileName, fileContent=fileContent))
        self.__dbSession.commit()
        self.__dbSession.add(UserTracks(userName=artist, trackName=fileName))
        self.__dbSession.commit()

    def deleteArtistAudioFile(self, trackName, artist):
        self.__dbSession.delete(self.__dbSession.query(Track).filter_by(trackName=trackName))
        self.__dbSession.commit()
        self.__dbSession.delete(self.__dbSession.query(UserTracks).filter_by(trackName=trackName, userName=artist))
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

    # User management

    def addUser(self, userName, password, name, lastName, age):
        newUserData = User_Data(userName=userName, name=name, lastName=lastName, age=age)
        newUserLogin = User_Login(userName=userName, password=password)

        self.__dbSession.add(newUserData)
        self.__dbSession.commit()
        self.__dbSession.add(newUserLogin)
        self.__dbSession.commit()

    def deleteUser(self, userName):
        self.__dbSession.delete(self.__dbSession.query(User_Data).filter_by(userName=userName).first())
        self.__dbSession.commit()

    def updateUser(self, userName, keyAndValues):
        self.__dbSession.query(User_Data).filter(User_Data.userName == userName).update(keyAndValues)
        self.__dbSession.commit()

    def getUser(self, userName):
        return getUserParse(self.__dbSession.query(User_Data).filter_by(userName=userName).first())

    def getPlaylistWithSubString(self, subString):
        return getPlaylistWithSubString(
            self.__dbSession.query(Playlist).filter(Playlist.playlistName.like("%" + subString + "%")).all())

    def addAlbum(self, albumName, albumYear, albumOwner):
        newAlbumData = Album(albumName=albumName, albumYear=albumYear)
        newAlbumUserData = AlbumUser(albumName=albumName, ownerName=albumOwner)
        self.__dbSession.add(newAlbumData)
        self.__dbSession.commit()
        self.__dbSession.add(newAlbumUserData)
        self.__dbSession.commit()

    # Album managment

    def getAlbumLikeName(self, albumName):
        return getAlbumLikeNameParser(
            self.__dbSession.query(Album).filter(Album.albumName.like("%" + albumName + "%")).all())

    def deleteAlbum(self, albumName):
        itemToBeDeleted = self.__dbSession.query(Album).filter_by(albumName=albumName).first()
        if (itemToBeDeleted != None):
            self.__dbSession.delete(itemToBeDeleted)
            self.__dbSession.commit()

