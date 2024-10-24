from flask_restful import fields
from helpers.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from sqlalchemy import func

# Campos para serialização
notificacoesFields = {
    'id': fields.Integer,
    'descricao': fields.String,
    'visualizado': fields.Boolean,
    'id_admin': fields.Integer
}

class Notificacoes(db.Model):
    __tablename__ = "notificacoes"
  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String, nullable=False)  # Removida a restrição de unicidade
    visualizado = db.Column(db.Boolean, nullable=False, server_default='false')
    # Referência da Chave Estrangeira
    id_admin = db.Column(db.Integer, db.ForeignKey('usuarios.id'))  # Atualizado o nome da tabela
    usuario = relationship('Usuario', backref='minhas_notificacoes', lazy=True)  # Renomeado aqui