from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import configparser 

app = Flask(__name__)
app.config['DEBUG'] = True

dbconfig = configparser.ConfigParser()
dbconfig.read("db-info.ini")
uristring = dbconfig.get("dbconfig","mysecret")
app.config['SQLALCHEMY_DATABASE_URI']= uristring
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)

class Post(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    title=db.Column(db.String(120))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime)
    draft=db.Column(db.Boolean, default=True)

    def __init__(self, title, content, draft):
        self.title=title
        self.content=content
        self.draft=draft


@app.route('/', methods=['POST', 'GET'])
def index():
    return "<h1>Shalom</h1>"

if __name__ == '__main__':
    app.run()
