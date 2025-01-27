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


    return app
