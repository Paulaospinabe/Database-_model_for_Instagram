import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    username = Column(String(25))
    firstname = Column(String(25))
    lastname  = Column(String(25))
    email = Column(String(30), nullable=False)
    

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.ID'))
    user_to_id = Column(Integer, ForeignKey('User.ID'))
    User = relationship(User)
   

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    user_id = Column(Integer, ForeignKey('User.ID'))
    User = relationship(User)
    

class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    Comment_text = Column(String(2000))
    author_id = Column(Integer, ForeignKey('User.ID'))
    post_id = Column(Integer, ForeignKey('Post.ID'))
    User = relationship(User)
    Post = relationship(Post)

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(primary_key=True)
    type = Column(String(50))
    url = Column(String(200))
    post_id = Column(Integer, ForeignKey('Post.ID'))
    Post = relationship(Post)
    



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e