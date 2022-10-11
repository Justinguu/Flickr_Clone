from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import User, Image, Comment

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(first_name="Nate", last_name="Scott", email="nscott1010@gmail.com", username="nate", password="password", previewImageUrl="URL")
    db.session.add(user)
    db.session.commit()

    image_1 = Image(userId=1, title="Nates first image", description="Beautiful", previewImageUrl="URL")
    image_2 = Image(userId=1, title="Nates second image", description="Wonderful", previewImageUrl="URL")

    images = [image_1, image_2]
    for image in images:
        db.session.add(image)
        db.session.commit()

    comment_1 = Comment(userId=1, imageId=1, body="Good shit")
    comment_2 = Comment(userId=1, imageId=1, body="Love it!")

    comments = [comment_1, comment_2]

    for comment in comments:
        db.session.add(comment)
        db.session.commit()
