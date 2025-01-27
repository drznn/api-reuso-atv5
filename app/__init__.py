from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar rotas
    from .routes import setup_routes
    setup_routes(app)

    with app.app_context():
        db.create_all()  # Garante que o banco de dados e as tabelas serão criados automaticamente

        # Popula o banco com cursos iniciais
        from .models import Curso
        if not Curso.query.first():  # Verifica se o banco está vazio
            cursos_iniciais = [
                Curso(titulo="Engenharia de Software", descricao="Curso avançado de desenvolvimento", carga_horaria=200),
                Curso(titulo="Design Digital", descricao="Curso sobre design gráfico e digital", carga_horaria=150),
            ]
            db.session.bulk_save_objects(cursos_iniciais)
            db.session.commit()

    return app
