from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user







app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demoAppDb.db' # sqlite database
app.config['SECRET_KEY'] = 'your_secret_key' #nøkel
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #to the login route if not logged in


class Textify(db.Model):
    id=db.Column(db.Integer,unique=True,primary_key=True)
    text=db.Column(db.String(25),nullable=False)
    username=db.Column(db.String(25),unique=True,nullable=False)


class Registartionform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    apti="hyftytfty"
    jdh = Textify(text=apti)
    db.add(jdh)
    db.commit()
    


if __name__ == '__main__':
    app.run(debug=True)