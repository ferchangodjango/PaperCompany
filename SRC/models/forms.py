from wtforms import Form
from wtforms import StringField, IntegerField,EmailField,validators


class FormSells(Form):
    IDPRODUCTS=IntegerField('IDPRODUCTS',[validators.NumberRange(min=14)])
    IDSELLER=IntegerField('IDESELLER',[validators.NumberRange(min=41)])
    QUANTITY=IntegerField('QUANTITY',[validators.NumberRange(min=1,max=100)])