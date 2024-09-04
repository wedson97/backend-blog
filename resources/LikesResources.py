from flask_restful import Resource, reqparse, marshal
from models.Like import Like, likeFields
from helpers.database import db


class LikesResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('post_id', type=int, help='Problema no id do post', required=True)
        self.parser.add_argument('usuario_id', type=int, help='Problema no id do usuário', required=True)
    

    def post(self):
        args = self.parser.parse_args()
        try:
            post_id = args["post_id"]
            usuario_id = args["usuario_id"]

            like = Like(post_id=post_id, usuario_id=usuario_id)

            db.session.add(like)
            db.session.commit()


            return marshal(like, likeFields)
        except Exception as e:
            print(e)

class LikeResources(Resource):
    
    def get(self, post_id):
        try:
            like = Like.query.filter_by(post_id=post_id).all()
            return marshal(like, likeFields)
        except Exception as e:
            print(e)
    
    def delete(self, post_id):
        try:
            like = Like.query.filter_by(usuario_id=post_id).first()  # Retorna o primeiro objeto correspondente
            if like:
                db.session.delete(like)
                db.session.commit()
                return {'Mensagem': 'Like deletado com sucesso'}
            else:
                return {'Mensagem': 'Like não encontrado'}, 404
        except Exception as e:
            print(e)
            return {'Mensagem': 'Erro ao deletar like'}, 500