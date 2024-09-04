from flask_restful import fields
from helpers.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

categoriaFields = {
    'id': fields.Integer,
    'nome': fields.String
}


class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Categoria {self.nome}>"