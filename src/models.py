import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250), nullable=False)
    Apellidos = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    Nick = Column(String(250), nullable=False)
    Contraseña = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    User_from_id = Column(Integer, ForeignKey('user.id'))
    User_to_id = Column(Integer, ForeignKey('user.id'))
    Followers = relationship(User)
    


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'))
    Post = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    Comments = relationship(Post)

class Like(Base):
    __tablename__ = 'like'    
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    Like = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    media = relationship(Post)



    def to_dict(self):
       return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e