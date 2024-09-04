from flask_restful import fields
from helpers.database import db
from sqlalchemy.sql import func

comentarioFields = {
    'id': fields.Integer,
    'post_id': fields.Integer,
    'autor_id': fields.Integer,
    'conteudo': fields.String,
    'criado_em': fields.String,
    'deletado_em': fields.String
}

class Comentario(db.Model):
    __tablename__ = 'comentarios'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    conteudo = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.TIMESTAMP, server_default=func.now())
    deletado_em = db.Column(db.TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"<Comentario {self.id}>"
