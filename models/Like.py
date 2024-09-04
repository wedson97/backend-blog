from flask_restful import fields
from helpers.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

likeFields = {
    'post_id': fields.Integer,
    'usuario_id': fields.Integer
}

class Like(db.Model):
    __tablename__ = 'likes'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    def __repr__(self):
        return f"<Like post_id={self.post_id} usuario_id={self.usuario_id}>"
