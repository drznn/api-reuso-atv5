from flask_restful import Resource
from flask import request
from app.models import Curso, db

class CursoResource(Resource):
    def get(self, curso_id=None):
        """Retorna um curso específico ou todos os cursos."""
        try:
            if curso_id:
                curso = Curso.query.get(curso_id)
                if not curso:
                    return {"message": "Curso não encontrado"}, 404
                return curso.to_dict()
            return [curso.to_dict() for curso in Curso.query.all()]
        except Exception as e:
            return {"message": f"Erro ao buscar cursos: {str(e)}"}, 500

    def post(self):
        """Adiciona um novo curso."""
        try:
            data = request.json
            novo_curso = Curso(**data)
            db.session.add(novo_curso)
            db.session.commit()
            return novo_curso.to_dict(), 201
        except Exception as e:
            return {"message": f"Erro ao adicionar curso: {str(e)}"}, 500

    def put(self, curso_id):
        """Atualiza os dados de um curso existente."""
        try:
            curso = Curso.query.get(curso_id)
            if not curso:
                return {"message": "Curso não encontrado"}, 404
            data = request.json
            for key, value in data.items():
                setattr(curso, key, value)
            db.session.commit()
            return curso.to_dict()
        except Exception as e:
            return {"message": f"Erro ao atualizar curso: {str(e)}"}, 500

    def delete(self, curso_id):
        """Remove um curso do banco de dados."""
        try:
            curso = Curso.query.get(curso_id)
            if not curso:
                return {"message": "Curso não encontrado"}, 404
            db.session.delete(curso)
            db.session.commit()
            return {"message": "Curso deletado"}
        except Exception as e:
            return {"message": f"Erro ao deletar curso: {str(e)}"}, 500
