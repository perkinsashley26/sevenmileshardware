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
    name= StringField('Name',[validators.DataRequired()])
    price= DecimalField('Price', [validators.DataRequired()])
    stock= IntegerField('Stock', [validators.DataRequired()])
    description= TextAreaField('Description', [validators.DataRequired()])
    prod_image = FileField('Photo Upload', validators= [FileAllowed(['jpg','png','Images only!'])])
    
