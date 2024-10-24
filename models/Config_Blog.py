from flask_restful import fields
from helpers.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

Config_BlogFields = {
    'id': fields.Integer,
    'nome_blog': fields.String,
    'cor_primaria': fields.String,
    'cor_secundaria': fields.String,
    'imagem_fundo': fields.String,
    'cor_fundo_primaria': fields.String,
    'cor_fundo_secundaria': fields.String
}

class Config_Blog(db.Model):
    __tablename__ = 'config_blog'

    id = db.Column(db.Integer, primary_key=True)
    nome_blog = db.Column(db.String, nullable=True)
    cor_primaria = db.Column(db.String, nullable=True)
    cor_secundaria = db.Column(db.String, nullable=True)
    imagem_fundo = db.Column(db.String, nullable=True)
    cor_fundo_primaria = db.Column(db.String, nullable=True)
    cor_fundo_secundaria = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Config id={self.id}>"
