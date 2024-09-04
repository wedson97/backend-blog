from flask_restful import fields
from helpers.database import db
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

postFields = {
    'id': fields.Integer,
    'titulo': fields.String,
    'conteudo': fields.String,
    'imagem_url': fields.String,
    'autor_id': fields.Integer,
    'criado_em': fields.String,
    'deletado_em': fields.String
}

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    imagem_url = db.Column(db.String)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    criado_em = db.Column(db.TIMESTAMP, server_default=func.now())
    deletado_em = db.Column(db.TIMESTAMP, nullable=True)

    # Relacionamentos
    comentarios = relationship('Comentario', backref='post', lazy=True)
    likes = relationship('Like', backref='post', lazy=True)
    deslikes = relationship('Deslike', backref='post', lazy=True)
    categorias = relationship('Categoria', secondary='post_categorias', backref='posts')

    def __repr__(self):
        return f"<Post {self.titulo}>"
