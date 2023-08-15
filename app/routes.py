from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.db.db import add_turnier, get_turniere_pro_spiel, get_turniere, get_scoretyp, get_runden_pro_spiel_pro_turnier, get_turniername, get_teilnehmerid_pro_turnier, get_punkte_pro_spiel_pro_turnier, get_spielliste_pro_turnier, get_punkteliste, get_teilnehmerid, add_teilnehmer, get_all_teilnehmer, delete_teilnehmer, add_spiel, get_all_spiele, delete_spiel, get_spiel, get_teilgenommene_turniere_pro_teilnehmer, edit_ergebnis, add_runde, delete_runde, get_last_round, get_spielid, add_game_to_turnier, delete_game_from_turnier, get_teilnehmername, execute_sql_file
from app.logik.gruppenerstellung import Gruppenerstellung
from app.logik.ergebnisberechnung import Ergebnisberechnung_gesamt, evaluate_points
import urllib.parse
import sqlite3
import os
from app.forms import TeilnehmerNeuForm, DeleteForm, SpielNeuForm, TurnierNeuForm, ErgebnisForm, TurnierBearbeiten, Turnierbaum

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
#----------Daten holen
	spielliste_pro_turnier = get_spielliste_pro_turnier(turnierid)
	punkteliste = get_punkteliste(turnierid)
	turniername = get_turniername(turnierid)[0][0]

	punkteliste_pro_spiel = []
	spielliste_to_delete = []
	for i in spielliste_pro_turnier:
		spielliste_to_delete.append(i[1])
		punkteliste_pro_spiel.append(get_punkte_pro_spiel_pro_turnier(turnierid=turnierid, spielid=i[0]))
	total_points = Ergebnisberechnung_gesamt(punkteliste_pro_spiel)

	punkteliste_pro_spiel_mit_points = Ergebnisberechnung_gesamt(punkteliste_pro_spiel, returnType="perGame")


	spielliste_to_add_db = get_all_spiele()
	spielliste_to_add = []
	for data in spielliste_to_add_db:
		spielliste_to_add.append(data[0])

	teilnehmerliste = get_teilnehmerid_pro_turnier(turnierid)

#----------Form initieren
	form = TurnierBearbeiten()
	form.gamelist_to_delete.choices = spielliste_to_delete
	form.gamelist_to_add.choices = spielliste_to_add

#----------Form Daten verarbeiten
	if request.method == "POST":
		if request.form.get('addgame'):
			print("Add Game")
			game_to_add = get_spielid(form.gamelist_to_add.data)[0][0]
			for teilnehmer in teilnehmerliste:
				flash(add_game_to_turnier(turnierid=turnierid, spielid=game_to_add, teilnehmerid=teilnehmer))
			return redirect(url_for('turnier', turnierid=turnierid))

		if request.form.get('deletegame'):
			print("Delete Game")
			game_to_delete = get_spielid(form.gamelist_to_delete.data)[0][0]
			flash(delete_game_from_turnier(turnierid=turnierid, spielid=game_to_delete))
			return redirect(url_for('turnier', turnierid=turnierid))



	return render_template('tournament.html', title="Turnier", total_points=total_points, punktelistespiel=punkteliste_pro_spiel_mit_points, spielliste=spielliste_pro_turnier, turnierid=turnierid, form=form, turniername=turniername)


@app.route('/turnier/ergebnistabelle/<turnierid>/<spielname>', methods=['POST', 'GET'])
def ergebnis(turnierid, spielname):
#----------Daten holen
	scoretyp=["kills", "zeit", "platz", "pvp", "punkte"] #todo: aus db ziehen?
	spiel = get_spiel(name=spielname)
	spielid = spiel[0][0]
	turniername = get_turniername(turnierid)
	runden_pro_spiel = [i[0] for i in get_runden_pro_spiel_pro_turnier(spielid=spielid, turnierid=turnierid)]
	anzahl_runden = len(runden_pro_spiel)
	punkteliste_db = get_punkte_pro_spiel_pro_turnier(turnierid=turnierid, spielid=spielid)
	punkteliste=[]
	for runde in punkteliste_db:
		punkteliste += runde #todo: sql statement ändern statt hier?
	print("punkteliste", punkteliste)
	anzahl_einträge = len(punkteliste)
	anzahl_teilnehmer = len(punkteliste_db[0])

#----------Gruppenerstellung, grad noch nicht relevant
	maxspieler = spiel[0][3]
	teilnehmerliste_id = get_teilnehmerid_pro_turnier(turnierid)
	print("teilnehmerliste_id", teilnehmerliste_id)
	print("turnierid", turnierid)
	teilnehmerliste = []
	for id in teilnehmerliste_id:
		teilnehmerliste.append(get_teilnehmername(id)[0][0])
	gruppen = Gruppenerstellung(Teilnehmerliste=teilnehmerliste, maxSpieler=maxspieler)

#----------Form initieren
	form = ErgebnisForm(ergebnislist=[{} for _ in range(anzahl_einträge)], deleteroundlist=[{} for _ in range(anzahl_runden)])
	form.rounds.choices = runden_pro_spiel
	form.scoretyp.choices = scoretyp
	form.scoretyp.data = punkteliste[0][2]

#----------Form Daten verarbeiten
	#for x in request.form:
	#	print("request.form", x)
	#print("form.validate_on_submit()", form.validate_on_submit())
	#print("request.form.get", request.form.get)
	#print("request.method", request.method)

	if request.form.get('submit'): #and form.validate_on_submit() 
		current_round = None

		for item in form.data['ergebnislist']:
		    if item['runde'] != '0':
		        current_round = item['runde']
		    else:
		        item['runde'] = current_round

		    print('scoretyp: ', form.scoretyp.data)
		    print('runde: ', item['runde'])
		    print('ergebnis: ', item['ergebnis'])
		    print('teilnehmer: ', item['teilnehmer'])
		    print('teilnehmerid:', get_teilnehmerid(item['teilnehmer'])[0][0])
		    print('..................')

		    flash(edit_ergebnis(turnierid=turnierid, spielid=spielid, teilnehmerid=get_teilnehmerid(item['teilnehmer'])[0][0], runde=item['runde'], score=item['ergebnis'], scoretyp=form.scoretyp.data))
		return redirect(url_for('ergebnis', turnierid=turnierid, spielname=spielname))

	if request.method == "POST":
		if request.form.get('addround'):
			print("Add Round")
			letzte_runde = get_last_round(turnierid=turnierid, spielid=spielid)[0][0]
			for teilnehmerid in teilnehmerliste_id:
				flash(add_runde(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid, runde=letzte_runde+1,scoretyp=form.scoretyp.data))
			return redirect(url_for('ergebnis', turnierid=turnierid, spielname=spielname))

		if request.form.get('deleteround'):
			print("Delete Round")
			flash(delete_runde(turnierid=turnierid, spielid=spielid, runde=form.rounds.data))
			return redirect(url_for('ergebnis', turnierid=turnierid, spielname=spielname))


	return render_template('result.html', title="Ergebnis", form=form, turnierid=turnierid, spielname=spielname, turniername=turniername, punkteliste=punkteliste)

@app.route('/turnier/turnierbaum/<turnierid>/<spielname>', methods=['POST', 'GET'])
def turnierbaum(turnierid, spielname):
# Daten holen
	turniername = get_turniername(turnierid)
	form = Turnierbaum()
	return render_template('turnierbaum.html', title="Ergebnis", turniername=turniername, form=form)

@app.route('/turnier_neu', methods=["POST", "GET"])
def turnier_neu():
	form = TurnierNeuForm()
	form.teilnehmer.choices=[(t[1]) for t in get_all_teilnehmer()]
	if form.validate_on_submit():
		flash(add_turnier(turniername=form.name.data, teilnehmerlist=form.teilnehmer.data))
		return redirect(url_for('turniere'))
	return render_template('tournament_new.html', title="Turnier hinzufügen", form=form)


@app.route('/turniere')
def turniere():
	turniere = get_turniere()
	return render_template('tournament_all.html', title="Turniere", turniere=turniere)


@app.route('/profil/<nickname>', methods=["POST", "GET"])
def profil(nickname):
	teilnehmerid = get_teilnehmerid(nickname)
	teilgenommene_turniere = get_teilgenommene_turniere_pro_teilnehmer(teilnehmerid[0][0])
	form = DeleteForm()
	if form.validate_on_submit():
		flash(delete_teilnehmer(nickname))
		return redirect(url_for('teilnehmer'))
	return render_template('player_profile.html', nickname=nickname, form=form, teilgenommene_turniere = teilgenommene_turniere)


@app.route('/teilnehmer_neu', methods=["POST", "GET"])
def teilnehmer_neu():
	form = TeilnehmerNeuForm()
	name=form.name.data
	nickname=form.nickname.data
	if form.validate_on_submit():
		flash(add_teilnehmer(name, nickname))
	return render_template('player_new.html', title="Teilnehmer hinzufügen", form=form)

@app.route('/teilnehmer', methods=["POST", "GET"])
def teilnehmer():
	alle_teilnehmer = get_all_teilnehmer()
	return render_template('player_all.html', title="Alle Teilnehmer Übersicht", alle_teilnehmer=alle_teilnehmer)


@app.route('/spiele')
def spiele():
	alle_spiele = get_all_spiele()
	return render_template('game_all.html', title="Alle Spiele Übersicht", alle_spiele=alle_spiele)

@app.route('/spiele/<spiel>', methods=["POST", "GET"])
def spiel(spiel):
	form = DeleteForm()
	if form.validate_on_submit():
		flash(delete_spiel(spiel))
		return redirect(url_for('spiele'))
	spieldetails = get_spiel(spiel)
	turniere = get_turniere_pro_spiel(spieldetails[0][0])
	return render_template('game.html', title=spiel, form=form, spiel=spiel, spieldetails=spieldetails, turniere=turniere)

@app.route('/spiel_neu', methods=["POST", "GET"])
def spiel_neu():
	form = SpielNeuForm()
	name=form.name.data
	typ=form.typ.data
	maxspieler=form.maxspieler.data
	if form.validate_on_submit():
		flash(add_spiel(name=name, typ=typ, maxspieler=maxspieler))
	return render_template('game_new.html', title="Spiel hinzufügen", form=form)

@app.route('/admin', methods=["POST", "GET"])
def admin():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	tables_file=os.path.join(current_dir, 'db', 'tables.sql')
	testdata_file=os.path.join(current_dir, 'db', 'testdata.sql')
	if request.method == 'POST':
		print(request.form)
		#data = request.form['testdata'] #theoretisch, hab nur buttons :D
		if 'tables' in request.form:
			print("tables")
			flash(execute_sql_file(sqlfile=tables_file, message="Tabellen erfolgreich resettet!"))
		if 'testdata.x' in request.form or 'testdata.y' in request.form:
			print("testdata")
			flash(execute_sql_file(sqlfile=testdata_file, message="Testdaten erfolgreich hinzugefügt!"))
	return render_template('admin.html', title="Admin Zeugs")