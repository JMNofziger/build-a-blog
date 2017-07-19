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
    body=db.Column(db.Text)
    date=db.Column(db.DateTime)
    draft=db.Column(db.Boolean, default=True)

    def __init__(self, title, body, draft):
        self.title=title
        self.body=body
        self.draft=draft


@app.route('/', methods=['GET'])
def index():
    return render_template("blog.html", title="JMN BAB Blog")

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    #TODO: After submitting a new post, your app displays the main blog page.
    #TODO: You're able to submit a new post.
    #TODO: If title or body is left empty the form is rendered again, with a helpful error message and any previously-entered content preserved
    return render_template("new-post.html")

@app.route('/blog', methods=['GET'])
def get_posts():
    #TODO: displays all the blog posts
    return render_template('all-posts.html')

if __name__ == '__main__':
    app.run()
