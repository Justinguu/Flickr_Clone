from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(25), nullable=False)
    last_name = db.Column(db.VARCHAR(25), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    username = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(25), nullable=False)
    previewImageUrl = db.Column(db.VARCHAR(500), nullable=False)

    # images = db.relationship('Image', back_populates='user')
    images = db.relationship('Image')

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.VARCHAR(100), nullable=False)
    description = db.Column(db.VARCHAR(1000))
    previewImageUrl = db.Column(db.VARCHAR(500), nullable=False)

    # user = db.relationship('User', back_populates='images')

# class Comment(db.Model):
#     __tablename__ = 'comments'

#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, nullable=False)
#     imageId = db.Column(db.Integer, nullable=False)
#     body = db.Column(db.VARCHAR(500))

#     users = db.relationship('Menu',)
