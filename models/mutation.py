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
        pierna_habil = String(required=None)
        fk_equipo = Int(required=True)
    
    jugadores = Field(lambda: Jugadores)                                          # Persona: se utiliza para definir cómo se mapea el modelo PersonaModel (tabla de la bd) en GraphQL, se importa de objects.py

    def mutate(self, info, name, last_name, edad, fk_equipo , pierna_habil=None):                      # lambda: crea una funcion anonima, lambda parametros: expresion, lambda: expresion (sin parametros)
        jugadores = JugadoresModel(name=name, last_name=last_name, edad=edad, fk_equipo=fk_equipo ,pierna_habil=pierna_habil)   # PersonaModel: es la tabla "persona" creada de la base de datos, persona.py

        db.session.add(jugadores)
        db.session.commit()

        return createJugador(jugadores=jugadores)

class updateJugador(Mutation):
    class Arguments:
        jugador_id = Int(required=True)
        name = String()
        last_name = String()
        edad = Int()
        pierna_habil = String()
        fk_equipo = Int()
                                                                                    
    jugadores = Field(lambda: Jugadores)                                                 # Field() = se utiliza para definir un campo en un tipo de objeto GraphQL

    def mutate(self, info, jugador_id ,name=None, last_name=None, edad=None, pierna_habil=None, fk_equipo=None):
        jugadores = JugadoresModel.query.get(jugador_id)
        if jugadores:
            if name:
                jugadores.name = name
            if last_name:
                jugadores.last_name = last_name
            if edad:
                jugadores.edad = edad
            if pierna_habil:
                jugadores.pierna_habil = pierna_habil
            if fk_equipo:
                jugadores.fk_equipo = fk_equipo
            
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
        fk_tecnico = Int(required=True)
    
    equipos = Field(lambda: Equipos)                                          

    def mutate(self, info, name, pais, anio_fundacion, fk_tecnico):                      
        equipos = EquiposModel(name=name, pais=pais, anio_fundacion=anio_fundacion, fk_tecnico=fk_tecnico) 
        db.session.add(equipos)
        db.session.commit()

        return createEquipo(equipos=equipos)
    
class updateEquipo(Mutation):
    class Arguments:
        equipo_id = Int(required=True)
        name = String()
        pais = String()
        anio_fundacion = Int()
        fk_tecnico = Int()
                                                                                    
    equipos = Field(lambda: Equipos)                                                 

    def mutate(self, info, equipo_id ,name=None, pais=None, anio_fundacion=None, fk_tecnico=None):
        equipos = EquiposModel.query.get(equipo_id)
        if equipos:
            if name:
                equipos.name = name
            if pais:
                equipos.pais = pais
            if anio_fundacion:
                equipos.anio_fundacion = anio_fundacion
            if fk_tecnico:
                equipos.fk_tecnico = fk_tecnico
            
            db.session.add(equipos)
            db.session.commit()

        return updateEquipo(equipos=equipos)
    
class deleteEquipo(Mutation):
    class Arguments:
        equipo_id = Int(required=True)

    equipos = Field(lambda: Equipos)

    def mutate(self, info, equipo_id):
        equipos = EquiposModel.query.get(equipo_id)
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
        titulos = Int(required=None)
        # fk_equipo = Int(required=True)
    
    tecnicos = Field(lambda: Tecnicos)                                          

    def mutate(self, info, name, last_name, edad ,titulos=None):                      
        tecnicos = TecnicosModel(name=name, last_name=last_name, edad=edad, titulos=titulos) 
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
        # fk_equipo = Int()
                                                                                    
    tecnicos = Field(lambda: Tecnicos)                                                 

    def mutate(self, info, tecnico_id ,name=None, last_name=None, edad=None, titulos=None):
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
            # if fk_equipo:
            #     tecnicos.fk_equipo = fk_equipo
            
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