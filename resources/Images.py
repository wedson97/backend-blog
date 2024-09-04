from flask import Flask, send_from_directory, abort
from flask_restful import Resource, reqparse
import os

class ImageResource(Resource):
    def get(self, filename):
        filename = filename.lstrip('./')
        
        directory = os.path.join('./uploads')

        file_path = os.path.join(directory, os.path.basename(filename))
        
        if os.path.isfile(file_path):
            return send_from_directory(directory, os.path.basename(filename))
        else:
            abort(404, description="Arquivo não encontrado")


