from src.sqlAlchemyConnector.Connector import *


class DatabaseConnector:
    __instance = None

    @classmethod
    def __haveInstance(cls):
        return True if cls.__instance else False

    @classmethod
    def instance(cls):
        if not cls.__haveInstance():
            cls.__instance = DatabaseConnector()
            return cls.__instance
        return cls.__instance

    def __init__(self):
        self.__connector = Connector()

    # User managemet methods

    def addUser(self, userName, password, name, lastName):
        self.__connector.addUser(userName, password, name, lastName)

    def getUser(self, userName):
        return self.__connector.getUser(userName)

    def getUserLogin(self, userName):
        return self.__connector.getUserLogin(userName)

    def deleteUser(self, userName):
        return self.__connector.deleteUser(userName)

    def updateUserData(self, userName, userData):
        return self.__connector.updateUserData(userName, userData)

    def updateUserCredentials(self, userName, password):
        return self.__connector.updateUserCredentials(userName, password)

    def logginUser(self,userName,password):
        self.__connector.logginUser(userName, password)

    def loggoutUser(self,userName):
        self.__connector.loggoutUser(userName)

    def isLoggedin(self,userName):
        return self.__connector.isLoggedin(userName)

    # Playlist management methods

    def getPlaylistLikeName(self, playlistName):
        return self.__connector.getPlaylistLikeName(playlistName)

    def getAllPlaylists(self):
        return self.__connector.getAllPlaylists()

    def addPlaylist(self, playlistName, userName, description):
        self.__connector.addPlaylist(playlistName, userName, description)

    def getPlaylist(self, playlistName):
        return self.__connector.getPlaylist(playlistName)

    def updatePlaylist(self, playlistName, data):
        self.__connector.updatePlaylist(playlistName, data)

    def deletePlaylist(self, playlistName):
        self.__connector.deletePlaylist(playlistName)

    def getPlaylistWithSubString(self,subString):
        return self.__connector.getPlaylistWithSubString(subString)

    def addTracksToPlaylist(self, playlistName, tracksData):
        return self.__connector.addTracksToPlaylist(playlistName, tracksData)

    def deleteTracksFromPlaylist(self, playlistName, tracksData):
        return self.__connector.deleteTracksFromPlaylist(playlistName, tracksData)

    # Artist File management methods

    def addArtistAudioFile(self, fileName, isAudioFile, artist):
        return self.__connector.addArtistAudioFile(fileName, isAudioFile, artist)

    def deleteArtistAudioFile(self, filename, artist):
        return self.__connector.deleteArtistAudioFile(filename, artist)

    #Track methods
    def addTrack(self, owner, trackName, fileContent):
        self.__connector.addTrack(owner,trackName, fileContent)

    def deleteTrack(self, trackId):
        return self.__connector.deleteTrack(trackId)

    def getTrack(self,trackName):
        return self.__connector.getTrack(trackName)

    def getAllTracks(self):
        return self.__connector.getAllTracks();

    def getTrackLikeName(self,trackName):
        return self.__connector.getTrackLikeName(trackName)

    def updateTrack(self,trackId, data):
        return self.__connector.updateTrack(trackId,data)

    # Album methods
    def addAlbum(self, albumName, albumYear, albumOwner):
        self.__connector.addAlbum(albumName, albumYear, albumOwner)

    def getAlbumLikeName(self, albumName):
        return self.__connector.getAlbumLikeName(albumName)

    def deleteAlbum(self, albumName):
        return self.__connector.deleteAlbum(albumName)

    def getAlbum(self,albumId):
        return self.__connector.getAlbum(albumId)

    def updateAlbum(self,albumId,data):
        return self.__connector.updateAlbum(albumId,data)

    def getAllAlbums(self):
        return self.__connector.getAllAlbums()

    def addTracksToAlbum(self,albumId,tracksData):
        return self.__connector.addTracksToAlbum(albumId,tracksData)

    def getAlbumOwner(self,albumName):
        return self.__connector.getAlbumOwner(albumName)