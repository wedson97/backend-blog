from flask_restful import Resource, reqparse, marshal
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from models.Post import Post, postFields
from helpers.database import db
import os
import base64

class PostsResources(Resource):
    

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('titulo', type=str, help='Problema no título', required=True)
        self.parser.add_argument('conteudo', type=str, help='Problema no conteúdo', required=True)
        self.parser.add_argument('autor_id', type=int, help='Problema no autor', required=True)
        self.parser.add_argument('imagem', type=str, help='Problema na imagem', required=True)

    def get(self):
        post = Post.query.all()
        return {'posts': marshal(post, postFields)}

    def post(self):
        args = self.parser.parse_args()
        titulo = args['titulo']
        conteudo = args['conteudo']
        autor_id = args['autor_id']
        imagem_base64 = args['imagem']

        imagem_data = base64.b64decode(imagem_base64.split(',')[1])

        filename = secure_filename(f"{titulo}_{autor_id}.png")
        image_path = os.path.join('./uploads/', filename)

        with open(image_path, 'wb') as img_file:
            img_file.write(imagem_data)

        novo_post = Post(
            titulo=titulo,
            conteudo=conteudo,
            autor_id=autor_id,
            imagem_url=image_path
        )
        db.session.add(novo_post)
        db.session.commit()

        return {"message": "Post criado com sucesso", "post_id": novo_post.id}, 200


class PostResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('titulo', type=str, help='Problema no titulo do post', required=False)
        self.parser.add_argument('conteudo', type=str, help='Problema no conteudo', required=False)
        self.parser.add_argument('autor_id', type=str, help='Problema na autor_id', required=False)
        self.parser.add_argument('imagem', type=str, help='Problema na imagem', required=False)

    def get(self, post_id):
        post = Post.query.get(post_id)
        if post != None:
            return {'posts': marshal(post, postFields)}
        return {'Mensagem':'Post não encontrado'},404

    def put(self, post_id):
        args = self.parser.parse_args()
        post = Post.query.get(post_id)
        if not post:
            return {'message': 'Post não encontrado'}, 404

        try:
            autor_id = int(args['autor_id'])  # Convertendo para int
        except ValueError:
            return {'message': 'ID do autor inválido'}, 400

        titulo = args['titulo']
        conteudo = args['conteudo']
        if args["imagem"]!=None:
            imagem_base64 = args['imagem']

            # Decodificar a imagem base64
            imagem_data = base64.b64decode(imagem_base64.split(',')[1])

            # Criar um nome de arquivo seguro e um caminho para salvar a imagem
            filename = secure_filename(f"{titulo}_{str(autor_id)}.png")
            image_path = os.path.join('./uploads/', filename)

            # Salvar a imagem no diretório do backend
            with open(image_path, 'wb') as img_file:
                img_file.write(imagem_data)
            post.imagem_url=image_path
        post.titulo = titulo
        post.conteudo = conteudo
        db.session.add(post)
        db.session.commit()
        return {'message': 'Post atualizado com sucesso'}, 200
    
    def delete(self, post_id):
        try:
            post = id
            
            post = Post.query.get(post_id)
            if not post:
                return {'Post': 'Post não encontrada'}, 404
            
            
            db.session.delete(post)
            db.session.commit()

            return {'Post': 'Post excluído com sucesso'}, 200

        except Exception as e:
            print(e)

            
class PostUsuarioResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('titulo', type=str, help='Problema no titulo do post', required=True)
        self.parser.add_argument('conteudo', type=str, help='Problema no conteudo', required=True)
        self.parser.add_argument('autor_id', type=str, help='Problema na autor_id', required=True)

    def get(self, id):
        post = Post.query.filter_by(autor_id=id).all()
        if post != None:
            return {'posts': marshal(post, postFields)}
        print(marshal(post, postFields))
        return marshal(post, postFields)