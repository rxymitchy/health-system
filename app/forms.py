from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, TextAreaField, StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email

class ProgramForm(FlaskForm):
    name = StringField('Program Name', validators=[DataRequired()])
    submit = SubmitField('Add Program')

class ClientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    address = TextAreaField('Address')
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d')
    gender = SelectField('Gender', choices=[
        ('', 'Select Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    submit = SubmitField('Save Client')

class EnrollmentForm(FlaskForm):
    programs = SelectMultipleField(
        'Programs',
        coerce=int,
        validators=[DataRequired(message="Please select at least one program")],
        render_kw={"class": "form-select", "size": "8"}
    )
    submit = SubmitField('Confirm Enrollment')