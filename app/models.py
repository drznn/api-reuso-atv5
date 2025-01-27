from . import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Converte o objeto Curso para um dicionário."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "carga_horaria": self.carga_horaria
        }
