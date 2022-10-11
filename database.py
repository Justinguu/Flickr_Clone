from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import User, Image

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
        db.session.add(image_1)
        db.session.commit()
