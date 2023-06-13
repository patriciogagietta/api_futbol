from api_config import db


class Equipos(db.Model):
    __tablename__ = "equipos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    anio_fundacion = db.Column(db.Integer)
    fk_tecnico = db.Column(db.Integer, db.ForeignKey("tecnicos.id"))
    tecnicos = db.relationship("Tecnicos")