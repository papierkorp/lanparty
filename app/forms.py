from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectMultipleField, SelectField
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
    submit = SubmitField('Add')

class ErgebnisForm(FlaskForm):
    ergebnistyp = SelectField('Ergebnistyp:', validators=[DataRequired()], coerce=str)
    ergebnis = StringField('Ergebnis', validators=[DataRequired()], render_kw={"placeholder": "Ergebnis"})
    submit = SubmitField('Ergebnis abschicken')

class ErgebnisAddRundeForm(FlaskForm):
    nur_fuer_label = StringField("Weitere Runde hinzufügen:")
    submit = SubmitField('Runde hinzufügen')

class ErgebnisDeleteRundeForm(FlaskForm):
    runden = SelectField('Bestimmte Runde löschen:', validators=[DataRequired()], coerce=str)
    submit = SubmitField('Runde löschen')