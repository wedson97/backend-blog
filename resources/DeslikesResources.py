from flask_restful import Resource, reqparse, marshal
from models.Deslike import Deslike, deslikeFields
from helpers.database import db


class DeslikesResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('post_id', type=int, help='Problema no id do post', required=True)
        self.parser.add_argument('usuario_id', type=int, help='Problema no id do usuário', required=True)
    

    def post(self):
        args = self.parser.parse_args()
        try:
            post_id = args["post_id"]
            usuario_id = args["usuario_id"]

            deslike = Deslike(post_id=post_id, usuario_id=usuario_id)

            db.session.add(deslike)
            db.session.commit()


            return marshal(deslike, deslikeFields)
        except Exception as e:
            print(e)

class DeslikeResources(Resource):
    
    def get(self, post_id):
        try:
            deslike = Deslike.query.filter_by(post_id=post_id).all()
            return marshal(deslike, deslikeFields)
        except Exception as e:
            print(e)
    
    def delete(self, post_id):
        try:
            deslike = Deslike.query.filter_by(usuario_id=post_id).first()  # Retorna o primeiro objeto correspondente
            if deslike:
                db.session.delete(deslike)
                db.session.commit()
                return {'Mensagem': 'Deslike deletado com sucesso'}
            else:
                return {'Mensagem': 'Deslike não encontrado'}, 404
        except Exception as e:
            print(e)
            return {'Mensagem': 'Erro ao deletar deslike'}, 500