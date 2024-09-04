from flask_restful import Resource, reqparse, marshal
from models.Comentario import Comentario, comentarioFields
from helpers.database import db


class ComentariosResources(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('post_id', type=int, help='Problema no id do post', required=True)
        self.parser.add_argument('autor_id', type=int, help='Problema no id do autor', required=False)
        self.parser.add_argument('conteudo', type=str, help='Problema no id do autor', required=True)

    def post(self):
        args = self.parser.parse_args()
        try:
            post_id = args["post_id"]
            autor_id = args["autor_id"]
            conteudo = args["conteudo"]
            comentario = Comentario(post_id=post_id, autor_id=autor_id, conteudo=conteudo)

            db.session.add(comentario)
            db.session.commit()

            return marshal(comentario, comentarioFields)
        except Exception as e:
            print(e)

    

class ComentarioResources(Resource):

   
    def get(self, id):
        comentario = Comentario.query.filter_by(post_id=id).all()
        return {'comentario': marshal(comentario, comentarioFields)}
    
    def delete(self, id):
        try:
            comentario = Comentario.query.get(id)
            db.session.delete(comentario)
            db.session.commit()
            return {'Mensagem':'Comentario deletado com sucesso!'}
        except Exception as e:
            print(e)
