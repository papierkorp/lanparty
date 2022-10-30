from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired
 
class TeilnehmerNeuForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    submit = SubmitField('Add')

class DeleteForm(FlaskForm):
    submit = SubmitField('Löschen')

class SpielNeuForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    typ = StringField('Typ', validators=[DataRequired()])
    maxspieler = IntegerField('Maxspieler', validators=[DataRequired()])
    submit = SubmitField('Add')