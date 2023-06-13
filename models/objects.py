from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    String
)
from models.equipos import Equipos as EquiposModel
from models.jugadores import Jugadores as JugadoresModel
from models.tecnicos import Tecnicos as TecnicosModel

class Jugadores(SQLAlchemyObjectType):                                                        # se utiliza para definir cómo se mapea el modelo PersonaModel en GraphQL
    class Meta:
        model = JugadoresModel

class Equipos(SQLAlchemyObjectType):
    class Meta:
        model = EquiposModel
    anio_fundacion = String(description='año en que se fundo el equipo')

class Tecnicos(SQLAlchemyObjectType):                                                        # se utiliza para definir cómo se mapea el modelo PersonaModel en GraphQL
    class Meta:
        model = TecnicosModel
