from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .config import Configuration
from .models import db, User, Image

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def main():
    users = User.query.all()
    # print(users[0].username)
    user_images = Image.query.join(User).filter(User.first_name == "Nate")
    print(user_images)
    return render_template("main_page.html", user_images=user_images)
