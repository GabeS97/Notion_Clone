from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

class BoardForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    template = SelectField('template', choices=['Quick Note', 'Task List', 'Reading List', 'Journal', 'Personal Home'])
    name = StringField('name', validators=[DataRequired(message='Please enter an input into this field'), Length(min=5, max=30, message='The name of your board must be within the range of 5 characters and 30 characters')])
    description = StringField('description')
    icon= StringField('icon')
