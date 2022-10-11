from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import User, Image, Comment, Like, Tag

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

    like_1 = Like(userId=1, imageId=1)
    like_2 = Like(userId=1, imageId=2)

    likes = [like_1, like_2]

    for like in likes:
        db.session.add(like)
        db.session.commit()

    tag_1 = Tag(userId=1, imageId=1, body="#Dope")
    tag_2 = Tag(userId=1, imageId=1, body="#GoodShit")

    tags = [tag_1, tag_2]

    for tag in tags:
        db.session.add(tag)
        db.session.commit()
