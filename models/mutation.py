from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
    Float,
)
from api_config import (
    db,
)

from .objects import (
    Jugadores,
    Equipos,
    Tecnicos
)

from .jugadores import Jugadores as JugadoresModel
from .equipos import Equipos as EquiposModel
from .tecnicos import Tecnicos as TecnicosModel


class createJugador(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        edad = Int(required=True)
        equipo_name = String(required=True)
    
    jugadores = Field(lambda: Jugadores)                                          # Persona: se utiliza para definir cómo se mapea el modelo PersonaModel (tabla de la bd) en GraphQL, se importa de objects.py

    def mutate(self, info, name, last_name, edad, equipo_name):                      # lambda: crea una funcion anonima, lambda parametros: expresion, lambda: expresion (sin parametros)
        equipo = EquiposModel.query.filter_by(name=equipo_name).first()             
        jugadores = JugadoresModel(name=name, last_name=last_name, edad=edad, equipo_id=equipo.id)   # PersonaModel: es la tabla "persona" creada de la base de datos, persona.py

        db.session.add(jugadores)
        db.session.commit()

        return createJugador(jugadores=jugadores)

class updateJugador(Mutation):
    class Arguments:
        jugador_id = Int(required=True)
        name = String()
        last_name = String()
        edad = Int()
        equipo_name = String()
                                                                                    
    jugadores = Field(lambda: Jugadores)                                                 # Field() = se utiliza para definir un campo en un tipo de objeto GraphQL

    def mutate(self, info, jugador_id ,name=None, last_name=None, edad=None, equipo_name=None):
        jugadores = JugadoresModel.query.get(jugador_id)
        if jugadores:
            if name:
                jugadores.name = name
            if last_name:
                jugadores.last_name = last_name
            if edad:
                jugadores.edad = edad
            if equipo_name:
                equipo = EquiposModel.query.filter_by(name=equipo_name).first()
                jugadores.equipo_id = equipo.id
            
            db.session.add(jugadores)
            db.session.commit()

        return updateJugador(jugadores=jugadores)


class deleteJugador(Mutation):
    class Arguments:
        jugador_id = Int(required=True)

    jugadores = Field(lambda: Jugadores)

    def mutate(self, info, jugador_id):
        jugadores = JugadoresModel.query.get(jugador_id)
        if jugadores:
            db.session.delete(jugadores)
            db.session.commit()

        return deleteJugador(jugadores=jugadores)
    

# EQUIPOS

class createEquipo(Mutation):
    class Arguments:
        name = String(required=True)
        pais = String(required=True)
        anio_fundacion = Int(required=True)
    
    equipos = Field(lambda: Equipos)                                          

    def mutate(self, info, name, pais, anio_fundacion):                      
        equipos = EquiposModel(name=name, pais=pais, anio_fundacion=anio_fundacion) 
        db.session.add(equipos)
        db.session.commit()

        return createEquipo(equipos=equipos)
    
class updateEquipo(Mutation):
    class Arguments:
        id_equipos = Int(required=True)
        name = String()
        pais = String()
        anio_fundacion = Int()
                                                                                    
    equipos = Field(lambda: Equipos)                                                 

    def mutate(self, info, id_equipos ,name=None, pais=None, anio_fundacion=None):
        equipos = EquiposModel.query.get(id_equipos)
        if equipos:
            if name:
                equipos.name = name
            if pais:
                equipos.pais = pais
            if anio_fundacion:
                equipos.anio_fundacion = anio_fundacion
            
            db.session.add(equipos)
            db.session.commit()

        return updateEquipo(equipos=equipos)
    
class deleteEquipo(Mutation):
    class Arguments:
        id_equipos = Int(required=True)

    equipos = Field(lambda: Equipos)

    def mutate(self, info, id_equipos):
        equipos = EquiposModel.query.get(id_equipos)
        if equipos:
            db.session.delete(equipos)
            db.session.commit()

        return deleteEquipo(equipos=equipos)
    
#  TECNICOS

class createTecnico(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        edad = Int(required=True)
        titulos = Int(required=True)
        equipo_name  = String(required=True)
    
    tecnicos = Field(lambda: Tecnicos)                                          

    def mutate(self, info, name, last_name, edad ,titulos, equipo_name):   
        equipo = EquiposModel.query.filter_by(name=equipo_name).first()                       
        tecnicos = TecnicosModel(name=name, last_name=last_name, edad=edad, titulos=titulos, equipo_id=equipo.id) 

        db.session.add(tecnicos)
        db.session.commit()

        return createTecnico(tecnicos=tecnicos)
    
class updateTecnico(Mutation):
    class Arguments:
        tecnico_id = Int(required=True)
        name = String()
        last_name = String()
        edad = Int()
        titulos = Int()
        equipo_name = String()
                                                                                    
    tecnicos = Field(lambda: Tecnicos)                                                 

    def mutate(self, info, tecnico_id ,name=None, last_name=None, edad=None, titulos=None, equipo_name=None):
        tecnicos = TecnicosModel.query.get(tecnico_id)
        if tecnicos:
            if name:
                tecnicos.name = name
            if last_name:
                tecnicos.last_name = last_name
            if edad:
                tecnicos.edad = edad
            if titulos:
                tecnicos.titulos = titulos
            if equipo_name:
                equipo = EquiposModel.query.filter_by(name=equipo_name).first()
                tecnicos.equipo_name = equipo.id
            
            db.session.add(tecnicos)
            db.session.commit()

        return updateTecnico(tecnicos=tecnicos)
    
class deleteTecnico(Mutation):
    class Arguments:
        tecnico_id = Int(required=True)

    tecnicos = Field(lambda: Tecnicos)

    def mutate(self, info, tecnico_id):
        tecnicos = TecnicosModel.query.get(tecnico_id)
        if tecnicos:
            db.session.delete(tecnicos)
            db.session.commit()

        return deleteTecnico(tecnicos=tecnicos)
    

class Mutation(ObjectType):
    create_jugador = createJugador.Field()
    update_jugador = updateJugador.Field()
    delete_jugador = deleteJugador.Field()

    create_equipo = createEquipo.Field()
    update_equipo = updateEquipo.Field()
    delete_equipo = deleteEquipo.Field()

    create_tecnico = createTecnico.Field()
    update_tecnicos = updateTecnico.Field()
    delete_tecnicos = deleteTecnico.Field()