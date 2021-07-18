"""Forms for adopt application"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet Name", validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine"), ('other', 'Other')],
    )

    photo_url = StringField(
        "Photo URL", validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age", validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = TextAreaField(
        "Comments", validators=[Optional()],
    )

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional()],
    )

    available = BooleanField("Availability")