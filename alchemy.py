import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ac3r@localhost/sqlalchemy'
db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.String(200))
    data = db.Column('data',db.Text)

    def __init__(self, id,name,data):
        self.id = id
        self.name = name
        self.data = data