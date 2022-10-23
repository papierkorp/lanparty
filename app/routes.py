from flask import render_template, flash, redirect, url_for, request, g
from app import app
from db import add_teilnehmer
import sqlite3
import os

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

@app.route('/teilnehmer')
def teilnehmer():
	return render_template('index.html', title="Teilnehmer")

@app.route('/teilnehmer/teilnehmer_add', methods=["POST"])
def add_teilnehmer(name, nickname):
	name=request.form["name"]
	nickname=request.form["nickname"]
	query1 = "INSERT INTO teilnehmer VALUES('{name}', '{nickname}')".format(name=name, nickname=nickname)
	cursor.execute(query1)
	connection.commit()
	return render_template('add_teilnehmer.html', title="Teilnehmer hinzufügen")

@app.route('/Spiele')
def spiele():
	return render_template('index.html', title="Spiele")

