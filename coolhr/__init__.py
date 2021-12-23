import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate

app = Flask(__name__)

DATABASE_URL = 'sqlite:///database.db'

app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "Thisshouldbeasecret"),
    SQLALCHEMY_DATABASE_URI=DATABASE_URL,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    MAIL_SERVER="smtp.googlemail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    ADMINS=["CoolHR"],
)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from coolhr import routes  # noqa
