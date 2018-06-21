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


    # Artist management methods

    def addArtist(self,stageName,name,lastName,age):
        self.__connector.addArtist(stageName,name,lastName,age)

    def getArtist(self,stageName):
        return self.__connector.getArtist(stageName)

    def deleteArtist(self,stageName):
        return self.__connector.deleteArtist(stageName)

    # Playlist management methods

    def getPlaylistLikeName(self, playlistName):
        return self.__connector.getPlaylistLikeName(playlistName)

    def addPlaylist(self, playlistName, userName, description):
        self.__connector.addPlaylist(playlistName, userName, description)

    def deletePlaylist(self, playlistName):
        return self.__connector.deletePlaylist(playlistName)

    def getPlaylist(self, playlistName):
        return self.__connector.getPlaylist(playlistName)

    def addPlaylistAudioFile(self, audioFile, playlistName):
        return self.__connector.addPlaylistAudioFile(audioFile, playlistName)

    # Artist File management methods

    def addArtistAudioFile(self, fileName, isAudioFile, artist):
        return self.__connector.addArtistAudioFile(fileName, isAudioFile, artist)

    def deleteArtistAudioFile(self, filename, artist):
        return self.__connector.deleteArtistAudioFile(filename, artist)

    def addAudioFile(self, fileName, isAudioFile):
        return self.__connector.addAudioFile(fileName, isAudioFile)

    def deleteAudioFile(self, filename):
        return self.__connector.deleteAudioFile(filename)

    def getAudioFile(self,filename):
        return self.__connector.getAudioFile(filename)

    # User managemet methods

    def addUser(self,userName,password, name, lastName, age):
        self.__connector.addUser(userName,password, name, lastName, age)

    def deleteUser(self,userName):
        return self.__connector.deleteUser(userName)

    #Album methods

    def addAlbum(self,albumName,albumYear,albumOwner):
            self.__connector.addAlbum(albumName,albumYear,albumOwner)

    def getAlbumLikeName(self,albumName):
        return self.__connector.getAlbumLikeName(albumName)

    def deleteAlbum(self,albumName):
        return self.__connector.deleteAlbum(albumName)
