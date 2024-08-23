from api_config import db

class Equipos(db.Model):
    __tablename__ = "equipos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    anio_fundacion = db.Column(db.Integer, nullable=False)

    jugadores = db.relationship('Jugadores', backref='equipo', lazy=True)
    tecnico = db.relationship('Tecnicos', uselist=False, backref='equipo')
