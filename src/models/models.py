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
    userName = Column(String(40), primary_key=True)
    description = Column(String(100))

# class AudioFileByPlaylist(Base):
#     __tablename__ = 'AudioFileByPlaylist'
#     filename = Column(String(40), ForeignKey('AudioFile.filename', ondelete='CASCADE'), primary_key=True)
#     playlistName = Column(String(50), ForeignKey('Playlist.playlistName', ondelete='CASCADE'), primary_key=True)
#     created = Column(DateTime, default=func.now())
