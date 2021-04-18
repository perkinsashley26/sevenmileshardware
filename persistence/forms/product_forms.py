# Import base class for forms
from flask_wtf import FlaskForm

from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import (
    SubmitField,
    IntegerField,
    FloatField,
    StringField,
    TextAreaField,
    validators,
    DecimalField
)

class ProductForm(FlaskForm):
    """Form for adding products."""
    pass
