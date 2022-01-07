from enum import unique
from . import db 
from flask_login import UserMixin


class User(db.Model, UserMixin):
    #props for the user tbl
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
