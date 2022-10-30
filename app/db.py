import sqlite3

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

connection = sqlite3.connect("lanparty.db", check_same_thread=False)
cursor = connection.cursor()

def create_tables():
	query_createtable1 = 'create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text unique);'
	query_createtable2 = 'create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr text, sieger integer);'
	query_createtable3 = 'create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);'
	query_createtable4 = 'create table if not exists vturnierbaum(turnierid integer, spielid integer, teilnehmerid integer, runde integer, platz integer);'
	cursor.execute(query_createtable1)
	cursor.execute(query_createtable2)
	cursor.execute(query_createtable3)
	cursor.execute(query_createtable4)
	connection.commit()

def add_teilnehmer(name, nickname):
	query = "INSERT INTO teilnehmer (name, nickname) VALUES('{name}', '{nickname}')".format(name=name, nickname=nickname)
	message = "Teilnehmer erfolgreich angelegt."
	return execute_query(query=query, message=message)

def add_spiel(name, typ, maxspieler):
	query = "INSERT INTO spiel (name, typ, maxspieler) VALUES ('{name}', '{typ}', {maxspieler})".format(name=name, typ=typ, maxspieler=maxspieler)
	message = "Spiel erfolgreich hinzugefügt."
	return execute_query(query=query,message=message)

def get_all_teilnehmer():
	try:
		query = 'select name, nickname from teilnehmer;'
		cursor.execute(query)
		return cursor.fetchall()
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.close()

def get_all_spiele():
	try:
		query = 'select name, typ, maxspieler from spiel;'
		return cursor.execute(query)
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.close()

def get_spiel(name):
	try:
		query = 'select name, typ, maxspieler from spiel where name="{name}";'.format(name=name)
		cursor.execute(query)
		return cursor.fetchall()
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.close()

def delete_teilnehmer(nickname):
	query = "DELETE FROM teilnehmer WHERE nickname='{nickname}'".format(nickname=nickname)
	message = "Teilnehmer erfolgreich gelöscht."
	return execute_query(query=query, message=message)

def delete_spiel(spiel):
	query = "DELETE FROM spiel WHERE name='{spiel}'".format(spiel=spiel)
	message = "Teilnehmer erfolgreich gelöscht."
	return execute_query(query=query, message=message)

def execute_query(query,message):
	try:
		cursor.execute(query)
		connection.commit()
		return message
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.close()