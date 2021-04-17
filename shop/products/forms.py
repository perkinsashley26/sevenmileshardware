from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import Form,SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators,DecimalField


class Addproducts(Form):
    name= StringField('Name',[validators.DataRequired()])
    price= DecimalField('Price', [validators.DataRequired()])
    stock= IntegerField('Stock', [validators.DataRequired()])
    description= TextAreaField('Description', [validators.DataRequired()])
    image1 = FileField('Photo Upload 1', validators= [FileAllowed(['jpg','png','Images only!'])])
    image2 = FileField('Photo Upload 2', validators= [FileAllowed(['jpg','png','Images only!'])])
    image3 = FileField('Photo Upload 3', validators= [FileAllowed(['jpg','png','Images only!'])])