from flask import Flask
from helpers.api import api
from helpers.database import db, migrate
from helpers.cors import cors
from urllib.parse import quote
app = Flask(__name__)
# password = 'Wedsonsilva97@.'
# db_user = 'postgres.deervdsjlxwotqjlcfdi'
# db_host = 'aws-0-sa-east-1.pooler.supabase.com'
# db_port = '6543'
# db_name = 'blog'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{quote(password)}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5431/blog'

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
