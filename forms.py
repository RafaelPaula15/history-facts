"""Forms for history-facts app."""

from wtforms import validators, IntegerField, SelectField, TextAreaField
from flask_wtf import FlaskForm


class YearFactForm(FlaskForm):
    """Form for adding a new fact."""

    year = IntegerField('Enter a year',
                            [validators.NumberRange(min=1, max=2022, message="year must be greater than 0 and less than 2023"),
                             validators.required()])



class NoteForm(FlaskForm):
    """Form for adding a new note."""

    note = TextAreaField('Enter a note', [validators.optional(), validators.length(max=30)])