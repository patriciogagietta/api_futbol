from api_config import db

class Jugadores(db.Model):
    __tablename__ = "jugadores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
