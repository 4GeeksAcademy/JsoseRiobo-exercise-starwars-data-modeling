import os
import sys
from sqlalchemy import String, ForeignKey, Column, Integer, Enum
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key= True)
    user_name = Column(String(100), nullable=False)
    user_lastname = Column(String(100), nullable=False)
    user_favourite = Column(String, nullable=False)
    

class Planets(Base):
    __tablename__ = "planets"
    planet_id = Column(String(100), primary_key=True )
    planet_name = Column(String(100), nullable=False )
    planet_size = Column(String(100), nullable=False)
    planet_age = Column(Integer, nullable=False)
    

class Characters(Base):
    __tablename__ = "characters"
    character_id = Column(String(100), primary_key=True )
    character_name = Column(String(100), nullable=False )
    character_race = Column(String(100), nullable=False)
    character_age = Column(Integer, nullable=False)
    
class Vehicles(Base):
    __tablename__ = "vehicles"
    vehicle_id = Column(String(100), primary_key=True )
    vehicle_name = Column(String(100), nullable=False )
    vehicle_max_speed = Column(String(100), nullable=False)
    vehicle_price = Column(Integer, nullable=False)

class Favourites(Base):
    __tablename__ = "favourites"
    id = Column(String(100), primary_key=True )
    favourite_user = Column(Integer, ForeignKey("user.id"))
    favourite_planets= Column(Integer, ForeignKey("planets.planet_id"))
    favourite_characters= Column(Integer, ForeignKey("characters.character_id")) 
    favourite_vehicles= Column(Integer, ForeignKey("vehicles.vehicle_name")) 
    relationship_user = relationship(User)
    relationship_planet = relationship(Planets)
    relationship_character = relationship(Characters)
    relationship_vehicle = relationship(Vehicles)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
