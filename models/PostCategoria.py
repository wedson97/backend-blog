from flask_restful import fields
from helpers.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

postCategoriaFields = {
    'post_id': fields.Integer,
    'categoria_id': fields.Integer
}

class PostCategoria(db.Model):
    __tablename__ = 'post_categorias'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), primary_key=True)

    def __repr__(self):
        return f"<PostCategoria post_id={self.post_id} categoria_id={self.categoria_id}>"