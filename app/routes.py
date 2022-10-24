from flask import render_template, flash, redirect, url_for, request, g
from app import app
from app.db import add_teilnehmer
import sqlite3
import os
from app.forms import TeilnehmerAddForm

#lanparty.db
#spiel
#--spielid(int)
#--name(text)
#--typ(text)
#--maxspieler(int)
#teilnehmer
#--teilnehmerid(int)
#--name(text)
#--nickname(text)
#turnier
#--turnierid(int)
#--name(text)
#--jahr(text)
#--sieger(integer)
#vturnierbaum
#--turnierid(int)
#--spielid(int)
#--teilnehmerid(int)
#--runde(int)
#--platz(int)

connection = sqlite3.connect("lanparty.db")
cursor = connection.cursor()



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
	if form.validate_on_submit():
		flash("Na du")
	name=form.name.data
	nickname=form.nickname.data
	#name=request.form["name"]
	#nickname=request.form["nickname"]
	#query1 = "INSERT INTO teilnehmer VALUES('{name}', '{nickname}')".format(name=name, nickname=nickname)
	#cursor.execute(query1)
	#connection.commit()
	return render_template('teilnehmer_add.html', title="Teilnehmer hinzufügen", form=form)

@app.route('/teilnehmer_all')
def teilnehmer_all():
	return render_template('index.html', title="Teilnehmer")

@app.route('/spiele')
def spiele():
	return render_template('index.html', title="Spiele")

@app.route('/spiele_add')
def spiele_add():
	return render_template('index.html', title="Spiele")

@app.route('/spiele_all')
def spiele_all():
	return render_template('index.html', title="Spiele")

