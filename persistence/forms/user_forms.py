# Import base class for forms
from flask_wtf import FlaskForm

# Form field imports
from wtforms import (
    StringField,
    BooleanField,
    PasswordField,
    SubmitField
)

# Validator imports
from wtforms.validators import DataRequired

class Register(FlaskForm):
    """The form for Registration."""
    first_name = StringField('First Name', [validators.Length(min=4, max=25)])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    
class Login(FlaskForm):
    """The form to log in a user"""
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired()])
    