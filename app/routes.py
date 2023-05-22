from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.db.db import add_turnier, get_turniere_pro_spiel, get_turniere, get_ergebnistyp, get_runden_pro_spiel_pro_turnier, get_turniername, get_teilnehmer_pro_turnier, get_punkte_pro_spiel_pro_turnier, get_spielliste_pro_turnier, get_punkteliste, get_teilnehmerid, add_teilnehmer, get_all_teilnehmer, delete_teilnehmer, add_spiel, get_all_spiele, delete_spiel, get_spiel, create_tables, get_teilgenommene_turniere_pro_teilnehmer, edit_ergebnis, add_runde, delete_runde, get_last_round
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

	punkteliste_bearbeitet = Ergebnisberechnung(punkteliste_pro_spiel)

	return render_template('turnier.html', title="Turnier", punktelisteturnier=punkteliste_bearbeitet, punktelistespiel=punkteliste_pro_spiel, spielliste=spielliste_pro_turnier, turnierid=turnierid)


@app.route('/turnier/<turnierid>/<spielname>', methods=['POST', 'GET'])
def ergebnis(turnierid, spielname):
#----------Daten holen
	ergebnistyp=["kills", "zeit", "platz", "pvp", "punkte"] #todo: aus db ziehen?
	spiel = get_spiel(name=spielname)
	spielid = spiel[0][0]
	turniername = get_turniername(turnierid)
	runden_pro_spiel = [i[0] for i in get_runden_pro_spiel_pro_turnier(spielid=spielid, turnierid=turnierid)]
	anzahl_runden = len(runden_pro_spiel)
	punkteliste_db = get_punkte_pro_spiel_pro_turnier(turnierid=turnierid, spielid=spielid)
	punkteliste=[]
	for runde in punkteliste_db:
		punkteliste += runde #todo: sql statement ändern statt hier?
	anzahl_einträge = len(punkteliste)
	anzahl_teilnehmer = len(punkteliste_db[0])

#----------Gruppenerstellung, grad noch nicht relevant
	maxspieler = spiel[0][3]
	teilnehmerliste = get_teilnehmer_pro_turnier(turnierid)
	gruppen = Gruppenerstellung(Teilnehmerliste=teilnehmerliste, maxSpieler=maxspieler)

#----------Form initieren
	form = ErgebnisForm(ergebnislist=[{} for _ in range(anzahl_einträge)], deleteroundlist=[{} for _ in range(anzahl_runden)])
	form.rounds.choices = runden_pro_spiel
	form.ergebnistyp.choices = ergebnistyp
	form.ergebnistyp.data = punkteliste[0][2]

#----------Form Daten verarbeiten
	#for x in request.form:
	#	print("request.form", x)

	if form.validate_on_submit() and request.form.get('submit'):
		current_round = None

		for item in form.data['ergebnislist']:
		    if item['runde'] != '0':
		        current_round = item['runde']
		    else:
		        item['runde'] = current_round

		    #print('ergebnistyp: ', form.ergebnistyp.data)
		    #print('runde: ', item['runde'])
		    #print('ergebnis: ', item['ergebnis'])
		    #print('teilnehmer: ', item['teilnehmer'])
		    #print('teilnehmerid:', get_teilnehmerid(item['teilnehmer'])[0][0])
		    #print('..................')

		    flash(edit_ergebnis(turnierid=turnierid, spielid=spielid, teilnehmerid=get_teilnehmerid(item['teilnehmer'])[0][0], runde=item['runde'], ergebnis=item['ergebnis'], ergebnistyp=form.ergebnistyp.data))
		return redirect(url_for('ergebnis', turnierid=turnierid, spielname=spielname))

	if request.method == "POST":
		if request.form.get('addround'):
			print("Add Round")
			letzte_runde = get_last_round(turnierid=turnierid, spielid=spielid)[0][0]
			for teilnehmerid in teilnehmerliste:
				flash(add_runde(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid, runde=letzte_runde+1,ergebnistyp=form.ergebnistyp.data))
			return redirect(url_for('ergebnis', turnierid=turnierid, spielname=spielname))

		if request.form.get('deleteround'):
			print("Delete Round")
			flash(delete_runde(turnierid=turnierid, spielid=spielid, runde=form.rounds.data))
			return redirect(url_for('ergebnis', turnierid=turnierid, spielname=spielname))


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
		create_tables()
		#flash(add_teilnehmer(name, nickname))
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