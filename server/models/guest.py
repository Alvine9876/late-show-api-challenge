from ..app import db

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(120))
    appearances = db.relationship("Appearance", backref="guest", cascade="all, delete-orphan")
