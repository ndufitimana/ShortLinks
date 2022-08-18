from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, URL, Length

class InputForm(FlaskForm):
    long_url = StringField("Enter the long URL", validators=[DataRequired()])
    domain = StringField("shortlink.io")
    alias = StringField([validators.Length(min = 5, max=5)])
    submit = SubmitField("Create Short Link")
    #validators=[Length(max=5, message="Alias cannot be longer than 5 characters")]