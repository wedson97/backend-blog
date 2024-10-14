# from flask import Flask
# from helpers.api import api
# from helpers.database import db, migrate
# from helpers.cors import cors
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5431/blog'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
# migrate.init_app(app, db)

# cors.init_app(app)

# api.init_app(app)
    
# def create_tables():
#     with app.app_context():
#         db.create_all()

# create_tables()

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask
from helpers.api import api
from helpers.database import db, migrate
from helpers.cors import cors
import os
import psycopg2

app = Flask(__name__)

def test_postgresql_connection():
    try:
        conn = psycopg2.connect("postgresql://postgres:123456@localhost:5431/blog")
        conn.close()
        return True
    except psycopg2.OperationalError:
        return False

if test_postgresql_connection():
    print("Conectando ao PostgreSQL")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5431/blog'
else:
    print("PostgreSQL não disponível, usando SQLite")
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)
cors.init_app(app)
api.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

if __name__ == '__main__':
    app.run(debug=True)
