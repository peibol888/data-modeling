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

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    user_name = Column(String(250), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
## https://en.wikipedia.org/wiki/ISO/IEC_5218
class GenderEnum(enum.Enum):
    Not_known = 0
    Male = 1
    Female = 2
    Not_applicable = 9

## CHARACTERS
class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(Enum(GenderEnum))
    age = Column(Integer)
    race = Column(String(50))
    language = Column(String(50))
    height = Column(Integer)
    weight = Column(Float)
    eyes_color = Column(String(50)) 

class Fav_Characters(Base):
    __tablename__ = 'fav_characters'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

## VEHICLES
class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Fav_Vehicles(Base):
    __tablename__ = 'fav_vehicles'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

## PLANETS
class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    radius = Column(Float)
    population = Column(Integer)

class Fav_Planets(Base):
    __tablename__ = 'fav_planets'

    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')