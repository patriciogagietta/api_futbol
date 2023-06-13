from graphene import (
    ObjectType,
    String,
    Boolean,
    List,
    Int
)

from .objects import Jugadores, Equipos, Tecnicos
from .jugadores import Jugadores as JugadoresModel
from .equipos import Equipos as EquiposModel
from .tecnicos import Tecnicos as TecnicosModel

class Query(ObjectType):
    jugadores = List(lambda: Jugadores, last_name=String(), id=Int(), name=String(), order_by_last_name=Boolean(), order_by_edad=Boolean())
    equipos = List(lambda: Equipos, id=Int(), name=String(), pais=String(), order_by_name= Boolean())
    tecnicos = List(lambda: Tecnicos, id= Int(), name=String(), last_name=String(), edad=Int() ,titulos=Int(), order_by_titulos=Boolean())

    def resolve_jugadores(self, info, id=None, name=None, last_name=None, order_by_last_name=None, order_by_edad=None):
        query = Jugadores.get_query(info=info)
        if id:
            query = query.filter(JugadoresModel.id==id)
        if name:
            query = query.filter(JugadoresModel.name==name)
        if last_name:
            query = query.filter(JugadoresModel.last_name==last_name)
        if  order_by_last_name:
            query = query.order_by(JugadoresModel.last_name)
        if  order_by_edad:
            query = query.order_by(JugadoresModel.edad)
        return query.all()
    
    def resolve_equipos(self, info, id=None, name=None, pais=None, anio_fundacion=None, order_by_name=None):
        query = Equipos.get_query(info=info)
        if id:
            query = query.filter(EquiposModel.id==id)
        if name:
            query = query.filter(EquiposModel.name==name)
        if pais:
            query = query.filter(EquiposModel.pais==pais)
        if anio_fundacion:
            query = query.filter(EquiposModel.anio_fundacion==anio_fundacion)
        if order_by_name:
            query = query.order_by(EquiposModel.name)

        return query.all()
    
    def resolve_tecnicos(self, info, id=None, name=None, last_name=None, edad=None, titulos=None, order_by_titulos=None):
        query = Tecnicos.get_query(info=info)

        if id:
            query = query.filter(TecnicosModel.id==id)
        if name:
            query = query.filter(TecnicosModel.name==name)
        if last_name:
            query = query.filter(TecnicosModel.last_name==last_name)
        if titulos:
            query = query.filter(TecnicosModel.titulos==titulos)
        if order_by_titulos:
            query = query.order_by(TecnicosModel.titulos)

        return query.all()