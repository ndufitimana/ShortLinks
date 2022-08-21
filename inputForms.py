from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, URLField
#from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL, Length, ValidationError
from modal import Links 
from validators import url

class InputForm(FlaskForm):
    #long_url = StringField("Enter the long URL", validators=[DataRequired()])
    long_url = StringField("Enter the long URL", validators=[DataRequired()])
    domain = StringField()
    alias = StringField(validators=[Length(max=5)])
    submit = SubmitField("Create Short Link")
    #validators=[Length(max=5, message="Alias cannot be longer than 5 characters")]
    def validate_alias(self, alias):
        res = Links.query.filter_by(alias=alias.data).first()
        if res is not None:
            raise ValidationError('Alias already used')
    def validate_long_url(self, long_url):
        if not url(long_url.data):
            raise ValidationError('Invalid URL')
      