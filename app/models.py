from . import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)
