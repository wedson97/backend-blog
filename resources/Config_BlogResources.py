from flask_restful import Resource, reqparse, marshal
from models.Deslike import Deslike, deslikeFields
from helpers.database import db


class Config_BlogResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
    

    def post(self):
        pass

class Config_BlogResources(Resource):
    
    def get(self, post_id):
        pass
    
    def delete(self, post_id):
        pass