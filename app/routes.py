from flask import render_template, flash, redirect, url_for, request
from app import app
from app.db.db import add_turnier, get_turniere_pro_spiel, get_turniere, get_ergebnistyp, get_runden_pro_spiel_pro_turnier, get_turniername, get_teilnehmer_pro_turnier, get_punkte_pro_spiel_pro_turnier, get_spielliste_pro_turnier, get_punkteliste, get_teilnehmerid, add_teilnehmer, get_all_teilnehmer, delete_teilnehmer, add_spiel, get_all_spiele, delete_spiel, get_spiel, create_tables, get_teilgenommene_turniere_pro_teilnehmer, edit_ergebnis
from app.logik.gruppenerstellung import Gruppenerstellung
from app.logik.ergebnisberechnung import Ergebnisberechnung
import urllib.parse
import sqlite3
import os
from app.forms import TeilnehmerNeuForm, DeleteForm, SpielNeuForm, TurnierNeuForm, ErgebnisForm

#encoded_name = urllib.parse.quote(name)

#Ablauf
# Neues Turnier
## 1) In DB neues Turnier mit ID + Name + Jahr
## 2) pro Teilnehmer pro Spiel: neue turnierbaum Verknüpfung mit TurnierID + TeilnehmerID + SpielID
# Eintrag im Spieldetail vom Turnier
## 1) insert into verknüpfung where turnierid=, teilnehmerid=, spielid= values (rundennummer, platz)
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/turnier/<turnierid>', methods=['GET', 'POST'])
def turnier(turnierid):
	spielliste_pro_turnier = get_spielliste_pro_turnier(turnierid)
	punkteliste = get_punkteliste(turnierid)

	punkteliste_pro_spiel = []
	for i in spielliste_pro_turnier:
		punkteliste_pro_spiel.append(get_punkte_pro_spiel_pro_turnier(turnierid=turnierid, spielid=i[0]))
	print("punktelistespiel", punkteliste_pro_spiel)
	punkteliste_bearbeitet = Ergebnisberechnung(punkteliste_pro_spiel)
	#print("punkteliste_bearbeitet:", punkteliste_bearbeitet)

	return render_template('turnier.html', title="Turnier", punktelisteturnier=punkteliste_bearbeitet, punktelistespiel=punkteliste_pro_spiel, spielliste=spielliste_pro_turnier, turnierid=turnierid)



#punkteliste [
#	[
#		('Worms Armageddon', 'brandmeister', 'platz', 1, 1), 
#		('Worms Armageddon', 'papierkorp', 'platz', 1, 2), 
#		('Worms Armageddon', 'tobse', 'platz', 1, 3), 
#		('Worms Armageddon', 'sancho', 'platz', 1, 4), 
#		('Worms Armageddon', 'draham', 'platz', 1, 5)
#	], 
#	[
#		('Worms Armageddon', 'papierkorp', 'platz', 2, 1), 
#		('Worms Armageddon', 'sancho', 'platz', 2, 2), 
#		('Worms Armageddon', 'draham', 'platz', 2, 3), 
#		('Worms Armageddon', 'brandmeister', 'platz', 2, 4), 
#		('Worms Armageddon', 'tobse', 'platz', 2, 5)
#	]
#]


@app.route('/turnier/<turnierid>/<spielname>', methods=['POST', 'GET'])
def ergebnis(turnierid, spielname):
	ergebnistyp=["kills", "zeit", "platz", "pvp", "punkte"]
	spiel = get_spiel(name=spielname)
	spielid = spiel[0][0]
	maxspieler = spiel[0][3]
	teilnehmerliste = get_teilnehmer_pro_turnier(turnierid)
	anzahl_teilnehmer = len(teilnehmerliste)

	turniername = get_turniername(turnierid)
	runden_pro_spiel = [i[0] for i in get_runden_pro_spiel_pro_turnier(spielid=spielid, turnierid=turnierid)]
	punkteliste = get_punkte_pro_spiel_pro_turnier(turnierid=turnierid, spielid=spielid)
	anzahl_runden = len(punkteliste)
	anzahl_form = len(punkteliste[0][0]) * anzahl_runden

	gruppen = Gruppenerstellung(Teilnehmerliste=teilnehmerliste, maxSpieler=maxspieler)
	form = ErgebnisForm(ergebnislist=[{} for _ in range(anzahl_form)])

	for index, ergebnistyp_form in enumerate(form.ergebnislist):
		ergebnistyp_form.ergebnistyp.choices = ergebnistyp

	#for i in range(anzahl_runden):
	#	ergebnistyp_form.ergebnistyp.default = get_ergebnistyp(turnierid=turnierid, spielid=spielid, runde=i+1)[0][0]
	#	#funktioniert ned

	print("--------------------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------------------")
	print("punkteliste", punkteliste)
	print("----- punkteliste -----")
	for i in punkteliste:
		for j in i:
			print(j)
			print('..................')
	print("form.errors", form.errors)
	print("form.validate", form.validate())
	print("form.validate_on_submit()", form.validate_on_submit(),)
	print("request.method == 'POST'", request.method == 'POST')
	print("form.data", form.data)
	print("----- form.data -----")
	for ergebnis in form.data['ergebnislist']:
	    print('ergebnistyp: ', ergebnis['ergebnistyp'])
	    print('runde: ', ergebnis['runde'])
	    print('ergebnis: ', ergebnis['ergebnis'])
	    print('teilnehmer: ', ergebnis['teilnehmer'])
	    print('..................')
	print("--------------------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------------------")

	#formdata = request.form
	#print("formdata", formdata)

	if form.validate_on_submit():
		print("pleaaaaaaaaase")
		name = form.name.data
		print("name", name)

	return render_template('ergebnis.html', title="Ergebnis", form=form, turnierid=turnierid, spielname=spielname, turniername=turniername, punkteliste=punkteliste)

@app.route('/turnier_neu', methods=["POST", "GET"])
def turnier_neu():
	form = TurnierNeuForm()
	form.teilnehmer.choices=[(t[1]) for t in get_all_teilnehmer()]
	if form.validate_on_submit():
		flash(form.name.data)
		flash(form.teilnehmer.data)
		flash(add_turnier(turniername=form.name.data, teilnehmerlist=form.teilnehmer.data))
		return redirect(url_for('turniere'))
	return render_template('turnier_neu.html', title="Turnier hinzufügen", form=form)


@app.route('/turniere')
def turniere():
	turniere = get_turniere()
	return render_template('turniere.html', title="Turniere", turniere=turniere)


@app.route('/profil/<nickname>', methods=["POST", "GET"])
def profil(nickname):
	teilnehmerid = get_teilnehmerid(nickname)
	teilgenommene_turniere = get_teilgenommene_turniere_pro_teilnehmer(teilnehmerid[0][0])
	form = DeleteForm()
	if form.validate_on_submit():
		flash(delete_teilnehmer(nickname))
		return redirect(url_for('teilnehmer'))
	return render_template('profil.html', nickname=nickname, form=form, teilgenommene_turniere = teilgenommene_turniere)


@app.route('/teilnehmer_neu', methods=["POST", "GET"])
def teilnehmer_neu():
	form = TeilnehmerNeuForm()
	name=form.name.data
	nickname=form.nickname.data
	if form.validate_on_submit():
		#create_tables()
		flash(add_teilnehmer(name, nickname))
	return render_template('teilnehmer_neu.html', title="Teilnehmer hinzufügen", form=form)

@app.route('/teilnehmer', methods=["POST", "GET"])
def teilnehmer():
	alle_teilnehmer = get_all_teilnehmer()
	return render_template('teilnehmer.html', title="Alle Teilnehmer Übersicht", alle_teilnehmer=alle_teilnehmer)


@app.route('/spiele')
def spiele():
	alle_spiele = get_all_spiele()
	return render_template('spiele.html', title="Alle Spiele Übersicht", alle_spiele=alle_spiele)

@app.route('/spiele/<spiel>', methods=["POST", "GET"])
def spiel(spiel):
	form = DeleteForm()
	if form.validate_on_submit():
		flash(delete_spiel(spiel))
		return redirect(url_for('spiele'))
	spieldetails = get_spiel(spiel)
	turniere = get_turniere_pro_spiel(spieldetails[0][0])
	return render_template('spiel.html', title=spiel, form=form, spiel=spiel, spieldetails=spieldetails, turniere=turniere)

@app.route('/spiel_neu', methods=["POST", "GET"])
def spiel_neu():
	form = SpielNeuForm()
	name=form.name.data
	typ=form.typ.data
	maxspieler=form.maxspieler.data
	if form.validate_on_submit():
		flash(add_spiel(name=name, typ=typ, maxspieler=maxspieler))
	return render_template('spiel_neu.html', title="Spiel hinzufügen", form=form)