from flask_restful import Resource
from flask import request
from app.models import Curso, db

class CursoResource(Resource):
    def get(self, curso_id=None):
        if curso_id:
            curso = Curso.query.get(curso_id)
            return vars(curso) if curso else {"message": "Curso não encontrado"}, 404
        return [vars(curso) for curso in Curso.query.all()]

    def post(self):
        data = request.json
        novo_curso = Curso(**data)
        db.session.add(novo_curso)
        db.session.commit()
        return vars(novo_curso), 201

    def put(self, curso_id):
        curso = Curso.query.get(curso_id)
        if not curso:
            return {"message": "Curso não encontrado"}, 404
        data = request.json
        for key, value in data.items():
            setattr(curso, key, value)
        db.session.commit()
        return vars(curso)

    def delete(self, curso_id):
        curso = Curso.query.get(curso_id)
        if not curso:
            return {"message": "Curso não encontrado"}, 404
        db.session.delete(curso)
        db.session.commit()
        return {"message": "Curso deletado"}
