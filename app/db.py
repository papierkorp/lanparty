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
#--jahr(date)
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
	query_createtable2 = 'create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr date default (strftime(\'%m-%Y\')), sieger integer);'
	query_createtable3 = 'create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);'
	query_createtable4 = 'create table if not exists turnierdetails(turnierdetailsid integer primary key autoincrement, turnierid integer references turnier(turnierid), spielid integer references spiel(spielid), teilnehmerid integer references teilnehmer(teilnehmerid), runde integer, platz integer);'
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



def delete_teilnehmer(nickname):
	query = "DELETE FROM teilnehmer WHERE nickname='{nickname}'".format(nickname=nickname)
	message = "Teilnehmer erfolgreich gelöscht."
	return execute_query(query=query, message=message)

def delete_spiel(spiel):
	query = "DELETE FROM spiel WHERE name='{spiel}'".format(spiel=spiel)
	message = "Teilnehmer erfolgreich gelöscht."
	return execute_query(query=query, message=message)



def get_all_teilnehmer():
	query = 'select name, nickname from teilnehmer;'
	return execute_select_query(query)

def get_all_spiele():
	query = 'select name, typ, maxspieler from spiel;'
	return execute_select_query(query)

def get_spiel(name):
	query = 'select name, typ, maxspieler from spiel where name="{name}";'.format(name=name)
	return execute_select_query(query)

def get_teilgenommene_turniere_pro_teilnehmer(teilnehmerid):
	query= 'select turnier.turnierid, turnier.name, turnier.jahr from turnierdetails as t inner join turnier on t.turnierid = turnier.turnierid where t.teilnehmerid = {teilnehmerid} group by t.turnierid;'.format(teilnehmerid=teilnehmerid)
	return execute_select_query(query)

def get_teilnehmerid(nickname):
	query = 'select teilnehmerid from teilnehmer where nickname = "{nickname}";'.format(nickname=nickname)
	return execute_select_query(query)

def get_punkteliste(turnierid):
	query = 'select spiel.name, teilnehmer.name, "Runde: " || td.runde, "Platz: " || td.platz from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid} and td.platz is not NULL;'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_spielliste_pro_turnier(turnierid):
	query = 'select spiel.spielid, spiel.name from turnierdetails as td inner join turnier on td.turnierid = turnier.turnierid inner join spiel on td.spielid = spiel.spielid where td.turnierid = {turnierid} group by spiel.name;'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_punkte_pro_spiel_pro_turnier(turnierid, spielid):
	query = 'select spiel.name, teilnehmer.name, "Runde: " || td.runde, "Platz: " || td.platz from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid} and td.spielid={spielid} and td.platz is not NULL order by td.runde, td.platz;'.format(turnierid=turnierid, spielid=spielid)
	return execute_select_query(query)








def execute_query(query,message):
	try:
		cursor.execute(query)
		connection.commit()
		return message
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.close()

def execute_select_query(query):
	try:
		cursor.execute(query)
		return cursor.fetchall()
	except sqlite3.IntegrityError as e:
		return "Integrity Error: " + str(e)
	connection.close()