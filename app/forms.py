from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectMultipleField, SelectField, FieldList, FormField
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

class ErgebnisInputForm(FlaskForm):
    runde=StringField('Runde', validators=[DataRequired()], render_kw={"placeholder": "Runde", "readonly":"true"})
    ergebnis = StringField('Ergebnis', validators=[DataRequired()], render_kw={"placeholder": "Ergebnis"})
    teilnehmer=StringField('Teilnehmer',validators=[DataRequired()], render_kw={"placeholder": "Teilnehmer", "readonly":"true"})

class ErgebnisForm(FlaskForm):
    ergebnistyp = SelectField('Ergebnistyp', validators=[DataRequired()], coerce=str)
    ergebnislist=FieldList(FormField(ErgebnisInputForm))
    submit = SubmitField('Ergebnis abschicken')
    addround = SubmitField('Runde hinzufügen')
    deleteround = SubmitField('Runde löschen')
    rounds = SelectField('Runden', validators=[DataRequired()], coerce=int)

class TurnierBearbeiten(FlaskForm):
    addgame = SubmitField('Game hinzufügen')
    deletegame = SubmitField('Game löschen')
    gamelist_to_delete = SelectField('Spielliste zum Löschen', validators=[DataRequired()], coerce=str)
    gamelist_to_add = SelectField('Spielliste zum Hinzufügen', validators=[DataRequired()], coerce=str)