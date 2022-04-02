"""Forms for adopt app."""

from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf



class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name:")

    species = SelectField("Species:", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(), AnyOf(values=['cat', 'dog', 'porcupine'])])

    photo_url = StringField("Image_Url:", validators=[Optional(), URL()])

    age = SelectField("Age:", choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')], validators=[InputRequired(), AnyOf(values=['baby', 'young', 'adult', 'senior'])])

    notes = StringField("Notes:")


class EditPetForm(FlaskForm):
    """ Form for editing a pet """

    photo_url = StringField("Image_Url:", validators=[Optional(), URL()])

    notes = StringField("Notes:")

    available = BooleanField("Available:")