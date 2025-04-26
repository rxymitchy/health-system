from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email

class ProgramForm(FlaskForm):
    name = StringField('Program Name', validators=[DataRequired()])
    submit = SubmitField('Add Program')

class ClientForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add Client')

class EnrollmentForm(FlaskForm):
    programs = SelectMultipleField('Programs', coerce=int)
    submit = SubmitField('Enroll')