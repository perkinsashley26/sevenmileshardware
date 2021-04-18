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
    pass

class Login(FlaskForm):
    """The form to log in a user"""
    pass