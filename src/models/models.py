from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User_Data(Base):
    __tablename__ = 'User_Data'
    userName = Column(String(50), primary_key=True)
    name = Column(String(40))
    lastName = Column(String(40))

class User_Login(Base):
    __tablename__ = 'User_Login'
    userName = Column(String(50), ForeignKey('User_Data.userName',ondelete='CASCADE'),primary_key=True)
    password = Column(String(128))
    lastPassChange = Column(DateTime, default=func.now())

class Playlist(Base):
    __tablename__ = 'Playlist'
    playlistName = Column(String(50), primary_key=True)
    description = Column(String(100))

class PlaylistUser(Base):
    __tablename__ = 'PlaylistUser'
    playlistName = Column(String(50), ForeignKey('Playlist.playlistName', ondelete='CASCADE'), primary_key=True)
    userName = Column(String(50), ForeignKey('User_Data.userName', ondelete='CASCADE'), primary_key=True)

class Track(Base):
    __tablename__ = 'Track'
    trackName = Column(String(100), primary_key=True)
    fileContent = Column(String(100))
    releaseDate = Column(DateTime, default=func.now())

class UserTracks(Base):
    __tablename__ = 'UserTracks'
    userName = Column(String(40), ForeignKey('User_Data.userName',ondelete='CASCADE'),primary_key=True)
    trackName = Column(String(100),ForeignKey('Track.trackName',ondelete='CASCADE'),primary_key=True)
    uploaded = Column(DateTime, default=func.now())

class Album(Base):
    __tablename__ = 'Album'
    albumName = Column(String(50), primary_key=True)
    albumYear = Column(Integer())

class AlbumUser(Base):
    __tablename__ = 'AlbumUser'
    albumName = Column(String(50), ForeignKey('Album.albumName', ondelete='CASCADE'),primary_key=True)
    userName = Column(String(50), ForeignKey('User_Data.userName', ondelete='CASCADE'),primary_key=True)
