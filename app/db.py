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

def add_teilnehmer(id, name, nickname):
	connection = sqlite3.connect("lanparty.db")
	cursor = connection.cursor()
	query_createtables = """create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text);
				create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr text, sieger integer);
				create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);
				create table if not exists vturnierbaum(turnierid integer, spielid integer, teilnehmerid integer, runde integer, platz integer);
	"""
	cursor.execute(query_createtables)
	query1 = "INSERT INTO teilnehmer VALUES({id}, '{name}', '{nickname}')".format(id=id, name=name, nickname=nickname)
	cursor.execute(query1)
	connection.commit()