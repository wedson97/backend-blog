from flask import Flask, send_from_directory, abort
from flask_restful import Resource, reqparse, marshal
import os
from helpers.database import db
from models.Notificacoes import Notificacoes, notificacoesFields

class NotificacoesResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('descricao', type=str, help='Problema na descrição', required=False)
        self.parser.add_argument('id_admin', type=int, help='Problema no id_admin', required=False)

    def get(self, id):
        notificacoes = Notificacoes.query.filter_by(id_admin=id).all()
        return marshal(notificacoes, notificacoesFields)

    def put(self, id):
        args = self.parser.parse_args()
        notificacoes = Notificacoes.query.filter_by(id_admin=id, visualizado=False).all()
        for notificação in notificacoes:
            notificação.visualizado = True
            
        db.session.commit()
        return {"message": "Notificações visualizadas"}, 200

class NotificacaoResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('descricao', type=str, help='Problema na descrição', required=True)
        self.parser.add_argument('id_admin', type=int, help='Problema no id_admin', required=True)

    def post(self):
        args = self.parser.parse_args() 
        descricao = args['descricao']
        id_admin = args['id_admin']

        notificacao = Notificacoes(
            descricao=descricao,
            id_admin=id_admin,
        )
        db.session.add(notificacao)
        db.session.commit()

        return {"message": "Notificação criada"}, 200
    
    

