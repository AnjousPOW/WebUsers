from flask import Flask, render_template, request, redirect, url_for
from user import User
from messageForm import MessageForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

users = []   #массив пользователей

app.config['SECRET_KEY'] = 'Your secret key'


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_user', methods=['GET', 'POST'])
def products():
    form = MessageForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        name = request.form.get('name')
        surname = request.form.get('surname')
        password = request.form.get('password')
        age = request.form.get('Age')
        users.append(User(email, name, surname, password, age))
        return redirect(url_for('products'))

    return render_template('add_user.html', form=form)






@app.route('/users')
def users_handler():
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run()