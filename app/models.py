from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(25), nullable=False)
    last_name = db.Column(db.VARCHAR(25), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    username = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(25), nullable=False)
    previewImageUrl = db.Column(db.VARCHAR(500))

    # one-to-many; user has many images
    images = db.relationship('Image', backref='user')
    comments = db.relationship("Comment", backref='user')
    likes = db.relationship("Like", backref='user')
    tags = db.relationship("Tag", backref='user')



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.VARCHAR(100), nullable=False)
    description = db.Column(db.VARCHAR(1000))
    previewImageUrl = db.Column(db.VARCHAR(500), nullable=False)

    comments = db.relationship("Comment", backref='image')
    likes = db.relationship("Like", backref='image')
    tags = db.relationship("Tag", backref='image')

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    imageId = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False)
    body = db.Column(db.VARCHAR(500))

class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    imageId = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False)

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    imageId = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False)
    body = db.Column(db.VARCHAR(500))
