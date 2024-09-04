from flask_restful import Resource, reqparse, marshal
from models.Usuario import Usuario, usuarioFields
from helpers.database import db
from sqlalchemy.exc import IntegrityError

class UsuariosResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('nome_usuario', type=str, help='Problema no nome do usuário', required=True)
        self.parser.add_argument('email', type=str, help='Problema no email', required=True)
        self.parser.add_argument('senha', type=str, help='Problema na senha', required=True)
        self.parser.add_argument('admin', type=bool, help='Problema no admin', required=False)

    def get(self):
        usuarios = Usuario.query.all()
        return {'usuarios': marshal(usuarios, usuarioFields)}
    

    def post(self):
        args = self.parser.parse_args()
        try:
            nome_usuario = args["nome_usuario"]
            email = args["email"]
            senha = args["senha"]
            admin = args["admin"]
            # if (args["admin"]!=False):
            #     admin = args["admin"]
            # else:
            #     admin = False

            usuario = Usuario(nome_usuario=nome_usuario, email=email, senha=senha, admin=admin)

            db.session.add(usuario)
            db.session.commit()


            return marshal(usuario, usuarioFields)
        except IntegrityError as e:
            db.session.rollback()
            if 'usuarios_nome_usuario_key' in str(e.orig):
                print("Nome de usuário já existe. Escolha outro.")
                return {'Error': 'Nome de usuário já existe. Escolha outro.'}, 400
            elif 'usuarios_email_key' in str(e.orig):
                print("Email já existe. Escolha outro.")
                return {'Error': 'Email já existe. Escolha outro.'}, 400
            else:
                print(f"Erro ao inserir o usuário: {e}")
                return {'Error': 'Erro ao inserir o usuário'}, 400
            


class UsuarioResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('nome_usuario', type=str, help='Problema no nome do usuário', required=True)
        self.parser.add_argument('email', type=str, help='Problema no email', required=True)
        self.parser.add_argument('senha', type=str, help='Problema na senha', required=True)

    def get(self, id):
        usuarios = Usuario.query.get(id)
        return {'usuarios': marshal(usuarios, usuarioFields)}
    
    def put(self, id):
        args = self.parser.parse_args()
        try:
            usuario = Usuario.query.get(id)
            usuario.nome_usuario = args["nome_usuario"]
            usuario.email = args["email"]
            usuario.senha = args["senha"]

            db.session.add(usuario)
            db.session.commit()

            return marshal(usuario, usuarioFields)
        except Exception as e:
            print(e)

    def delete(self):
        pass

class UsuarioLoginResources(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('nome_usuario', type=str, help='Problema no nome do usuário', required=True)
        self.parser.add_argument('senha', type=str, help='Problema na senha', required=True)

    def post(self):
        args = self.parser.parse_args()
        nome_usuario = args["nome_usuario"]
        senha = args["senha"]

        if not nome_usuario:
            return {"message": "Nome de usuário não fornecido."}, 400

        if not senha:
            return {"message": "Senha não fornecida."}, 400

        try:
            usuario = Usuario.query.filter_by(nome_usuario=nome_usuario).first()

            # Verifica se o usuário existe
            if not usuario:
                return {"message": "Nome de usuário incorreto."}, 404

            # Verifica se a senha está correta
            if not usuario.senha == senha:
                return {"message": "Senha incorreta."}, 401

            return {'usuarios': marshal(usuario, usuarioFields)}
        except Exception as e:
            print(e)
            return {"message": "Erro interno do servidor."}, 500
        
    
