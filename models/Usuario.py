from flask_restful import fields
from helpers.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from sqlalchemy import func

usuarioFields = {
    'id': fields.Integer,
    'nome_usuario': fields.String,
    'email': fields.String,
    'admin':fields.Boolean
}

class Usuario(db.Model):
    __tablename__ = "usuarios"
  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, server_default="false")
    criado_em = db.Column(db.DateTime, server_default=func.now())
    deletado_em = db.Column(db.DateTime, nullable=True)
    
    # Relacionamentos
    posts = relationship('Post', backref='autor', lazy=True)
    comentarios = relationship('Comentario', backref='autor', lazy=True)
    likes = relationship('Like', backref='usuario', lazy=True)
    deslikes = relationship('Deslike', backref='usuario', lazy=True)
    notificacoes = relationship('Notificacoes', backref='usuario_ref', lazy=True)  # Mude aqui

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f"<Usuario {self.nome_usuario}>"