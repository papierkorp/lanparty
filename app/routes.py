from flask import render_template, flash, redirect, url_for, request, g
from app import app
from app.db import add_teilnehmer, get_all_teilnehmer, delete_teilnehmer, add_spiel, get_all_spiele, delete_spiel, get_spiel
import sqlite3
import os
from app.forms import TeilnehmerNeuForm, DeleteForm, SpielNeuForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/turnier_neu')
def turnier_neu():
	return render_template('turnier_neu.html', title="Turnier")

@app.route('/turniere')
def turniere():
	return render_template('turniere.html', title="Turniere")

@app.route('/turnier_aktiv')
def turnier_aktiv():
	return render_template('turnier_aktiv.html', title="Turnier")


@app.route('/profil/<nickname>', methods=["POST", "GET"])
def profil(nickname):
	#todo datenbank abfragen + infos anzeigen
	form = DeleteForm()
	if form.validate_on_submit():
		flash(delete_teilnehmer(nickname))
		return redirect(url_for('teilnehmer'))
	return render_template('profil.html', nickname=nickname, form=form)


@app.route('/teilnehmer_neu', methods=["POST", "GET"])
def teilnehmer_neu():
	form = TeilnehmerNeuForm()
	name=form.name.data
	nickname=form.nickname.data
	if form.validate_on_submit():
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