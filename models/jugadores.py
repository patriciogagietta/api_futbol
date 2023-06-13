from api_config import db


class Jugadores(db.Model):
    __tablename__ = "jugadores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    pierna_habil = db.Column(db.String(50), nullable=True)
    fk_equipo = db.Column(db.String, db.ForeignKey("equipos.id"))
    equipos = db.relationship("Equipos", backref='jugadores_equipo')
