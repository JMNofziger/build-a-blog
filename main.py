from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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
    date=db.Column(db.DateTime, nullable=False)
    draft=db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, title, body, draft):
        self.title=title
        self.body=body
        self.draft=draft
        self.date=datetime.now()

@app.route('/', methods=['GET'])
def index():
    posts = Post.query.all()
    return render_template("blog.html",posts=posts, title="JMN BAB Blog")

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    #TODO: After submitting a new post, your app displays the main blog page.
    #TODO: You're able to submit a new post.
    #TODO: If title or body is left empty the form is rendered again, with a helpful error message and any previously-entered content preserved
    if request.method == 'POST':
        post_title = request.form['title']
        post_body = request.form['body']
        post_draft = request.form.get('draft')
        new_post=Post(post_title,post_body,post_draft)
        db.session.add(new_post)
        db.session.commit()
    
    return render_template("new-post.html")

#@app.route('/single', methods=['POST','GET'])

@app.route('/blog', methods=['GET'])
def get_posts():
    #TODO: displays all the blog posts
    posts = Post.query.all()
    return render_template('all-posts.html', title="BAB Blog", posts=posts)

if __name__ == '__main__':
    app.run()
