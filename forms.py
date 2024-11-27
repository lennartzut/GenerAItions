from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(),
                                             Length(max=150)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo(
                                                     'password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(),
                                             Length(max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')