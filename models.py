"""Models for Adoption Agency"""

from flask_sqlalchemy import SQLAlchemy 

IMAGE_URL = 'https://image.flaticon.com/icons/png/512/1818/1818401.png'

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

#MODELS

class Pet(db.Model):
    """Pet"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image(self):
        """Image for pet or image provided"""

        return self.photo_url or IMAGE_URL

    