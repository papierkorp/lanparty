from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired
 
class TeilnehmerNeuForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    nickname = StringField('Nickname', validators=[DataRequired()], render_kw={"placeholder": "Nickname"})
    submit = SubmitField('Add')

class DeleteForm(FlaskForm):
    submit = SubmitField('Löschen')

class SpielNeuForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    typ = StringField('Typ', validators=[DataRequired()], render_kw={"placeholder": "Typ"})
    maxspieler = IntegerField('Maxspieler', validators=[DataRequired()], render_kw={"placeholder": "Maxspieler"})
    submit = SubmitField('Add')

class TurnierNeuForm(FlaskForm):
    name = StringField('Turnier-Name', validators=[DataRequired()], render_kw={"placeholder": "Turnier-Name"})
    teilnehmer = SelectMultipleField('Teilnehmer', validators=[DataRequired()], coerce=str)
    spielliste = SelectMultipleField('Spiele', validators=[DataRequired()], coerce=str)
    submit = SubmitField('Add')