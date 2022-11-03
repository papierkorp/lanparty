from flask import render_template, flash, redirect, url_for, request, g
from app import app
from app.db import get_punkte_pro_spiel_pro_turnier, get_spielliste_pro_turnier, get_punkteliste, get_teilnehmerid, add_teilnehmer, get_all_teilnehmer, delete_teilnehmer, add_spiel, get_all_spiele, delete_spiel, get_spiel, create_tables, get_teilgenommene_turniere_pro_teilnehmer
import sqlite3
import os
from app.forms import TeilnehmerNeuForm, DeleteForm, SpielNeuForm, TurnierNeuForm

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

@app.route('/turnier/<turnierid>')
def turnier(turnierid):
	#todo turniername
	#todo punkteliste übersichtlicher
	spielliste_pro_turnier = get_spielliste_pro_turnier(turnierid)
	punkteliste = get_punkteliste(turnierid)
	punkteliste_pro_spiel = []
	for i in spielliste_pro_turnier:
		punkteliste_pro_spiel.append(get_punkte_pro_spiel_pro_turnier(turnierid=turnierid, spielid=i[0]))
	print(punkteliste_pro_spiel)
	print(spielliste_pro_turnier)

	for spiel in spielliste_pro_turnier:
		for spielerg in punkteliste_pro_spiel:
			print("--------------spielerg für {spiel}".format(spiel=spiel))
			print(spielerg)
			for element in spiel:
				print("--------------element: ")
				print(element)
	return render_template('turnier.html', title="Turnier", punktelisteturnier=punkteliste, punktelistespiel=punkteliste_pro_spiel, spielliste=spielliste_pro_turnier)


@app.route('/turnier_neu', methods=["POST", "GET"])
def turnier_neu():
	form = TurnierNeuForm()
	form.spielliste.choices=[(s[0]) for s in get_all_spiele()]
	form.teilnehmer.choices=[(t[1]) for t in get_all_teilnehmer()]
	if form.validate_on_submit():
		flash(form.teilnehmer.data)
		flash(form.spielliste.data)
	return render_template('turnier_neu.html', title="Turnier", form=form)

@app.route('/turniere')
def turniere():
	return render_template('turniere.html', title="Turniere")

@app.route('/turnier_aktiv')
def turnier_aktiv():
	return render_template('turnier_aktiv.html', title="Turnier")


@app.route('/profil/<nickname>', methods=["POST", "GET"])
def profil(nickname):
	#todo datenbank abfragen + infos anzeigen
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
		return redirect(url_for('spiel'))
	spieldetails = get_spiel(spiel)
	print(spieldetails)
	return render_template('spiel.html', form=form, spiel=spiel, spieldetails=spieldetails)

@app.route('/spiel_neu', methods=["POST", "GET"])
def spiel_neu():
	form = SpielNeuForm()
	name=form.name.data
	typ=form.typ.data
	maxspieler=form.maxspieler.data
	if form.validate_on_submit():
		flash(add_spiel(name=name, typ=typ, maxspieler=maxspieler))
	return render_template('spiel_neu.html', title="Spiel hinzufügen", form=form)