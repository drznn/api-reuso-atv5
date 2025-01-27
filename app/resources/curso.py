from flask_restful import Resource
from flask import request
from app.models import Curso, db

class CursoResource(Resource):
    def get(self, curso_id=None):
        if curso_id:
            curso = Curso.query.get(curso_id)
            return curso.to_dict() if curso else {"message": "Curso não encontrado"}, 404
        return [curso.to_dict() for curso in Curso.query.all()]

    def post(self):
        data = request.json
        novo_curso = Curso(**data)
        db.session.add(novo_curso)
        db.session.commit()
        return novo_curso.to_dict(), 201

    def put(self, curso_id):
        curso = Curso.query.get(curso_id)
        if not curso:
            return {"message": "Curso não encontrado"}, 404
        data = request.json
        for key, value in data.items():
            setattr(curso, key, value)
        db.session.commit()
        return curso.to_dict()

    def delete(self, curso_id):
        curso = Curso.query.get(curso_id)
        if not curso:
            return {"message": "Curso não encontrado"}, 404
        db.session.delete(curso)
        db.session.commit()
        return {"message": "Curso deletado"}
