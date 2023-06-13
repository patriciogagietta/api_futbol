from api_config import db


class Tecnicos(db.Model):
    __tablename__ = "tecnicos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    titulos = db.Column(db.Integer, nullable=True)