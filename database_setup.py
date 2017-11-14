# Add User table to store User information in our Database for Local permission system

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    item_list = relationship("Item", cascade="all, delete-orphan")
    # Image
    # image_url = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):
    __tablename__ = 'catalog_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(500))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    # Image
    # image_url = Column(String, nullable=False)


    # Add our decorator method for out JSON response
    @property
    # Returns object data in easily serializable format
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id
        }


# Insert at end of file
engine = create_engine('postgres://jaehudkkwfzerl:845c5f6b7e9e9fe885d85565b15ff1229bdb55bde3a0ea885b06eb674ebe8984@ec2-176-34-111-152.eu-west-1.compute.amazonaws.com:5432/d48l6m5e8cmivs')

Base.metadata.create_all(engine)


