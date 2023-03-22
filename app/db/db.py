import sqlite3
import json

connection = sqlite3.connect("lanparty.db", check_same_thread=False)
cursor = connection.cursor()

def create_tables():
	query_createtable_teilnehmer = 'create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text unique);'
	query_createtable_turnier = 'create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr date default (strftime(\'%m-%Y\')), teilnehmer text sieger integer);'
	query_createtable_spiel = 'create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);'
	query_createtable_turnierdetails = 'create table if not exists turnierdetails(turnierdetailsid integer primary key autoincrement, turnierid integer references turnier(turnierid), spielid integer references spiel(spielid), teilnehmerid integer references teilnehmer(teilnehmerid), runde integer, ergebnistyp text, ergebnis integer);'
	cursor.execute(query_createtable_teilnehmer)
	cursor.execute(query_createtable_turnier)
	cursor.execute(query_createtable_spiel)
	cursor.execute(query_createtable_turnierdetails)
	connection.commit()
	connection.close()






def add_teilnehmer(name, nickname):
	query = "INSERT INTO teilnehmer (name, nickname) VALUES('{name}', '{nickname}')".format(name=name, nickname=nickname)
	message = "Teilnehmer {nickname} erfolgreich angelegt.".format(nickname=nickname)
	return execute_query(query=query, message=message)

def add_spiel(name, typ, maxspieler):
	query = "INSERT INTO spiel (name, typ, maxspieler) VALUES ('{name}', '{typ}', {maxspieler})".format(name=name, typ=typ, maxspieler=maxspieler)
	message = "Spiel {name} erfolgreich hinzugefügt.".format(name=name)
	return execute_query(query=query,message=message)

def add_turnier(turniername, teilnehmerlist):
	teilnehmerlist_ids = []
	for name in teilnehmerlist:
		teilnehmerlist_ids.append(str(get_teilnehmerid(name)[0][0]))
	teilnehmerlist_strg = " ".join(teilnehmerlist_ids)
	query = "INSERT INTO turnier(name, teilnehmer) VALUES ('{turniername}', '{teilnehmer}');".format(turniername=turniername, teilnehmer=teilnehmerlist_strg)
	message = "Turnier erfolgreich angelegt."
	return execute_query(query=query, message=message)


def delete_teilnehmer(nickname):
	query = "DELETE FROM teilnehmer WHERE nickname='{nickname}'".format(nickname=nickname)
	message = "Teilnehmer {nickname} erfolgreich gelöscht.".format(nickname=nickname)
	return execute_query(query=query, message=message)

def delete_spiel(spiel):
	query = "DELETE FROM spiel WHERE name='{spiel}'".format(spiel=spiel)
	message = "Spiel {spiel} erfolgreich gelöscht.".format(spiel=spiel)
	return execute_query(query=query, message=message)





#insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,1,1,1,45,"kills");
def edit_ergebnis(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp):
	query = "insert or replace into turnierdetails (turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (tuid,sid,teid,rd,{ergebnis}, ergebnistyp)".format(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid, runde=runde, ergebnis=ergebnis, ergebnistyp=ergebnistyp)
	message = "Spiel {spielid} für Turnier {turnierid} erfolgreich geupdated."
	return execute_query(query)






def get_turniere():
	query = 'select * from turnier;'
	return execute_select_query(query)

def get_turniername(turnierid):
	query = 'select name || " " || jahr from turnier where turnierid={turnierid};'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_all_teilnehmer():
	query = 'select name, nickname from teilnehmer;'
	return execute_select_query(query)

def get_all_spiele():
	query = 'select name, typ, maxspieler from spiel;'
	return execute_select_query(query)

def get_ergebnistyp(turnierid, spielid):
	query = 'select distinct(ergebnistyp) from turnierdetails where turnierid={turnierid} and spielid={spielid};'.format(turnierid=turnierid, spielid=spielid)
	return execute_select_query(query)

def get_spiel(name):
	query = 'select * from spiel where name="{name}";'.format(name=name)
	return execute_select_query(query)

def get_teilgenommene_turniere_pro_teilnehmer(teilnehmerid):
	query= 'select turnier.turnierid, turnier.name, turnier.jahr from turnierdetails as t inner join turnier on t.turnierid = turnier.turnierid where t.teilnehmerid = {teilnehmerid} group by t.turnierid;'.format(teilnehmerid=teilnehmerid)
	return execute_select_query(query)

def get_teilnehmerid(nickname):
	query = 'select teilnehmerid from teilnehmer where nickname = "{nickname}";'.format(nickname=nickname)
	return execute_select_query(query)

def get_punkteliste(turnierid):
	query = 'select spiel.name, teilnehmer.name, "Runde: " || td.runde, "Platz: " || td.ergebnis from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid};'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_spielliste_pro_turnier(turnierid):
	query = 'select spiel.spielid, spiel.name from turnierdetails as td inner join turnier on td.turnierid = turnier.turnierid inner join spiel on td.spielid = spiel.spielid where td.turnierid = {turnierid} group by spiel.name;'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_punkte_pro_spiel_pro_turnier(turnierid, spielid):
	gesamtergebnis = []
	anzahlrunden = execute_select_query('select max(runde) from turnierdetails where turnierid={turnierid} and spielid={spielid};'.format(turnierid=turnierid, spielid=spielid))
	for runde in range(1, anzahlrunden[0][0]+1):
		ergebnistyp = execute_select_query('select distinct(ergebnistyp) from turnierdetails where turnierid={turnierid} and spielid={spielid} and runde={runde};'.format(turnierid=turnierid, spielid=spielid, runde=runde))
		#print("ergebnistyp:", ergebnistyp[0][0])
		#print("runde:", runde)
		
		#platz = 1. Platz ganz oben
		#zeit = 1. Platz ganz oben
		#kills = 1. Platz ganz unten
		#pvp = 0/1
		#punkte = 1. Platz ganz unten

		query = 'select spiel.name, teilnehmer.nickname, td.ergebnistyp, td.runde, td.ergebnis from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid} and td.spielid={spielid} and td.runde={runde} order by td.runde, td.ergebnis;'.format(turnierid=turnierid, spielid=spielid, runde=runde)
		gesamtergebnis.append(execute_select_query(query))

		#if ergebnistyp[0][0] == "kills" or ergebnistyp[0][0] == "Punkte":
		#	print("gesamtergebnis kills/Punkte:", gesamtergebnis)
		#elif ergebnistyp[0][0] == "zeit" or ergebnistyp[0][0] == "platz":
		#	print("gesamtergebnis zeit:", gesamtergebnis)
		#elif ergebnistyp[0][0] == "pvp":
		#	print("gesamtergebnis pvp:", gesamtergebnis)

	return gesamtergebnis

def get_teilnehmer_pro_turnier(turnierid):
	query = 'select teilnehmer from turnier where turnierid={turnierid}'.format(turnierid=turnierid)
	teilnehmerstr = execute_select_query(query)
	return teilnehmerstr[0][0].split()

def get_runden_pro_spiel_pro_turnier(turnierid, spielid):
	query = 'select distinct(td.runde) from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid} and td.spielid={spielid} order by td.runde, td.ergebnis;'.format(turnierid=turnierid, spielid=spielid)
	return execute_select_query(query)

def get_turniere_pro_spiel(spielid):
	query = 'select distinct turnier.name, turnier.jahr from turnierdetails as v inner join turnier on v.turnierid = turnier.turnierid where v.spielid = {spielid};'.format(spielid=spielid)
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