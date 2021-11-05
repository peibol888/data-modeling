import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

## https://en.wikipedia.org/wiki/ISO/IEC_5218
class GenderEnum(enum.Enum):
    Unknown = 0
    Male = 1
    Female = 2
    Not_applicable = 9

## Media type
class MediaTypeEnum(enum.Enum):
    Unknown = 0
    Image = 1
    Video = 2
    Other = 3

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    user_name = Column(String(250), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    public_status = Column(String(250))

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)
    date = Column(DateTime(), default=datetime.now())

    author_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaTypeEnum))
    url = Column(String(1000))

    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)

## Draw from SQLAlchemy base
render_er(Base, 'diagram_instagram.png')