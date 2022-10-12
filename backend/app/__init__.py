from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .config import Configuration
from .models import db, User, Image, Comment, Like

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def main():
    user_images = Comment.query.join(User).filter(User.id == 1)
    return render_template("main_page.html", user_images=user_images)
