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
	query_add_teilnehmer = "INSERT INTO teilnehmer (name, nickname) VALUES('{name}', '{nickname}')".format(name=name, nickname=nickname)
	try:
		cursor.execute(query_add_teilnehmer)
		return "Teilnehmer erfolgreich angelegt."
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.commit()

def get_all_teilnehmer():
	query_get_all_teilnehmer = 'select name, nickname from teilnehmer;'
	cursor.execute(query_get_all_teilnehmer)
	result = cursor.fetchall()
	return result