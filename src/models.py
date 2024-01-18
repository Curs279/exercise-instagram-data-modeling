import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):  #parent
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    hash = Column(String, unique=True, nullable=False)

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User")
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user = relationship("User")
    post = relationship("Posts")

class Media(Base):
    __tablename__ ='media'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    post = relationship("Posts")

class Followers(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_to_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
