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

    def addArtist(self,stageName,name,lastName,age):
        self.__connector.addArtist(stageName,name,lastName,age)

    def getArtist(self,stageName):
        return self.__connector.getArtist(stageName)

    def deleteArtist(self,stageName):
        return self.__connector.deleteArtist(stageName)

    def addUser(self,userName,password, name, lastName, age):
        self.__connector.addUser(userName,password, name, lastName, age)

    def deleteUser(self,userName):
        return self.__connector.deleteUser(userName)