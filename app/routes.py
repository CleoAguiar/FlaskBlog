from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login solicitado pelo usuario {}, salvar= {}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Entrar', form=form)
