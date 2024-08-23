from api_config import db

class Tecnicos(db.Model):
    __tablename__ = "tecnicos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    titulos = db.Column(db.Integer, nullable=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), unique=True, nullable=True)
