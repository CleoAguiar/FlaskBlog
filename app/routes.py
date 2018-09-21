from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Cleo"}
    posts = [
        {
            "author": {"username": "Jhon"},
            "body": "Beutiful day in Brazil!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The movie was so cool!"    
        }
    ]

    return render_template("index.html", title="Página Inicial",
                           user=user, posts=posts)
