from flask import Flask
from helpers.api import api
from helpers.database import db, migrate
from helpers.cors import cors
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados e migrações
db.init_app(app)
migrate.init_app(app, db)

# Inicializando o CORS
cors.init_app(app)

# Inicializando as rotas da API
api.init_app(app)
    

# Função para criar as tabelas no banco de dados
def create_tables():
    with app.app_context():
        db.create_all()

# Chama a função para criar as tabelas
create_tables()

if __name__ == '__main__':
    app.run(debug=True)
