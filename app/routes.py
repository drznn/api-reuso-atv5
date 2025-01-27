from flask_restful import Api
from app.resources.curso import CursoResource

def setup_routes(app):
    api = Api(app)
    api.add_resource(CursoResource, '/cursos', '/cursos/<int:curso_id>')
