from flask import render_template, flash, redirect, url_for, request, g
from app import app
from app.db import add_teilnehmer, get_all_teilnehmer
import sqlite3
import os
from app.forms import TeilnehmerAddForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/turnier')
def turnier():
	return render_template('index.html', title="Turnier")

@app.route('/turnier_add')
def turnier_add():
	return render_template('turnier_add.html', title="Turnier")

@app.route('/turnier_all')
def turnier_all():
	return render_template('index.html', title="Turnier")

@app.route('/turnier_current')
def turnier_current():
	return render_template('index.html', title="Turnier")

@app.route('/teilnehmer')
def teilnehmer():
	return render_template('index.html', title="Teilnehmer")

@app.route('/teilnehmer/teilnehmer_add', methods=["POST", "GET"])
def teilnehmer_add():
	form = TeilnehmerAddForm()
	name=form.name.data
	nickname=form.nickname.data
	if form.validate_on_submit():
		add_teilnehmer(name, nickname)
	return render_template('teilnehmer_add.html', title="Teilnehmer hinzufügen", form=form)

@app.route('/teilnehmer_all')
def teilnehmer_all():
	alle_teilnehmer = get_all_teilnehmer()
	print(type(alle_teilnehmer))
	return render_template('teilnehmer_all.html', title="Alle Teilnehmer Übersicht", alle_teilnehmer=alle_teilnehmer)

@app.route('/spiele')
def spiele():
	return render_template('index.html', title="Spiele")

@app.route('/spiele_add')
def spiele_add():
	return render_template('index.html', title="Spiele")

@app.route('/spiele_all')
def spiele_all():
	return render_template('index.html', title="Spiele")

