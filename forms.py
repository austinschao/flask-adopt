"""Forms for adopt app."""

from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, ValidationError




class AddPetForm(FlaskForm):
    """Form for adding pets."""
    def validate_species(form, field):
        if field.data not in ["dog", "cat", "porcupine"]:
            raise ValidationError('Species must be either dog, cat or porcupine')

    name = StringField("Pet Name:")
    species = StringField("Species:", validators=[validate_species])
    photo_url = StringField("Image_Url:", validators=[Optional(), URL()])
    age = SelectField("Age:", choices=[('baby','Baby'),('young', 'Young'),('adult','Adult'),('senior','Senior')])
    notes = StringField("Notes:")

