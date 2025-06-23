from server.app import db


from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance


class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
