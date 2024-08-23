from flask_graphql import GraphQLView

from api_config import (
    app,
    db,
)
from models.schema import schema

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # ? Habilita la interfaz GraphiQL
    )
)


@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return 'Hola Mundo'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(host='localhost', port=5000, debug=True)