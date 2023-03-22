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
    ergebnistyp = SelectField('Ergebnistyp:', validators=[DataRequired()], coerce=str)
    runde=StringField('Runde', render_kw={"placeholder": "Runde", "disabled":"disabled"})
    ergebnis = StringField('Ergebnis', validators=[DataRequired()], render_kw={"placeholder": "Ergebnis"})
    teilnehmer=StringField('Teilnehmer', render_kw={"placeholder": "Teilnehmer", "disabled":"disabled"})

class ErgebnisForm(FlaskForm):
    ergebis=FieldList(FormField(ErgebnisInputForm, default=lambda: ErgebnisInputForm()), min_entries=1)
    submit = SubmitField('Ergebnis abschicken')

    def __init__(self, *args, **kwargs):
        super(ErgebnisForm, self).__init__(*args, **kwargs)
        if 'min_entries' in kwargs:
            self.ergebis.min_entries = kwargs['min_entries']