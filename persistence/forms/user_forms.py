# Import base class for forms
from flask_wtf import FlaskForm

# Form field imports
from wtforms import (
    StringField,
    BooleanField,
    PasswordField,
    SubmitField,
    validators
)

# Validator imports
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    """The form for Registration."""
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    
class LoginForm(FlaskForm):
    """The form to log in a user"""
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired()])
    