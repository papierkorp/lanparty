import sqlite3
import json

connection = sqlite3.connect("lanparty.db", check_same_thread=False)
cursor = connection.cursor()

def execute_sql_file(sqlfile, message):
	with open(sqlfile, 'r') as file:
		filedata = file.read().split(';')
		for statement in filedata:
			if statement.strip(): #leere Statements ignorieren
				try:
					cursor.execute(statement)
					connection.commit()
				except sqlite3.IntegrityError as e:
					return "Integrity Error: " + str(e)
		#connection.close()
	return message




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
	message = "Turnier {turniername} mit den Teilnehmer: {teilnehmerlist} erfolgreich angelegt.".format(turniername=turniername, teilnehmerlist=teilnehmerlist)
	return execute_query(query=query, message=message)

def delete_teilnehmer(nickname):
	query = "DELETE FROM teilnehmer WHERE nickname='{nickname}'".format(nickname=nickname)
	message = "Teilnehmer {nickname} erfolgreich gelöscht.".format(nickname=nickname)
	return execute_query(query=query, message=message)

def delete_spiel(spiel):
	query = "DELETE FROM spiel WHERE name='{spiel}'".format(spiel=spiel)
	message = "Spiel {spiel} erfolgreich gelöscht.".format(spiel=spiel)
	return execute_query(query=query, message=message)

def edit_ergebnis(turnierid, spielid, teilnehmerid, runde, score, scoretyp):
	#query = "insert or replace into turnierdetails (turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (tuid,sid,teid,rd,{score}, scoretyp)".format(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid, runde=runde, score=score, scoretyp=scoretyp)
	query="UPDATE turnierdetails SET scoretyp = '{scoretyp}', score = {score} WHERE turnierid={turnierid} and spielid={spielid} and runde={runde} and teilnehmerid={teilnehmerid};".format(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid, runde=runde, score=score, scoretyp=scoretyp)
	message = "Ergebnis: {score} für den Spieler {teilnehmername} in Runde {runde} erfolgreich geupdated.".format(score=score,  teilnehmername=get_teilnehmername(teilnehmerid)[0][0], runde=runde)
	return execute_query(query=query, message=message)

def add_runde(turnierid, spielid, teilnehmerid, runde, scoretyp):
	query = "insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, scoretyp, score) values ({turnierid},{spielid},{teilnehmerid},{runde},'{scoretyp}', 0)".format(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid, runde=runde, scoretyp=scoretyp)
	message = "Runde erfolgreich hinzugefügt."
	return execute_query(query=query,message=message)

def delete_runde(turnierid, spielid, runde):
	query = "delete from turnierdetails where turnierid={turnierid} and spielid={spielid} and runde={runde}".format(turnierid=turnierid, spielid=spielid, runde=runde)
	message = "Runde erfolgreich gelöscht."
	return execute_query(query=query,message=message)

def add_game_to_turnier(turnierid, spielid, teilnehmerid):
	query= "insert into turnierdetails(turnierid, spielid,teilnehmerid, runde, score, scoretyp) values ({turnierid},{spielid},{teilnehmerid},1,0,'kills');".format(turnierid=turnierid, spielid=spielid, teilnehmerid=teilnehmerid)
	message = "Spiel {spielname} mit Teilnehmer {teilnehmername} hinzugefügt.".format(spielname=get_spielname(spielid)[0][0], teilnehmername=get_teilnehmername(teilnehmerid)[0][0])
	return execute_query(query=query,message=message)

def delete_game_from_turnier(turnierid, spielid):
	query = "delete from turnierdetails where turnierid={turnierid} and spielid={spielid};".format(turnierid=turnierid, spielid=spielid)
	message = "Spiel {spielname} gelöscht.".format(spielname=get_spielname(spielid)[0][0])
	return execute_query(query=query,message=message)





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

def get_scoretyp(turnierid, spielid, runde):
	query = 'select distinct(scoretyp) from turnierdetails where turnierid={turnierid} and spielid={spielid} and runde={runde};'.format(turnierid=turnierid, spielid=spielid, runde=runde)
	return execute_select_query(query)

def get_spiel(name):
	query = 'select * from spiel where name="{name}";'.format(name=name)
	return execute_select_query(query)

def get_spielname(spielid):
	query = 'select name from spiel where spielid="{spielid}";'.format(spielid=spielid)
	return execute_select_query(query)

def get_spielid(spielname):
	query = 'select spielid from spiel where name="{spielname}";'.format(spielname=spielname)
	return execute_select_query(query)

def get_maxspieler(spielid):
	query = 'select maxspieler from spiel where spielid={spielid};'.format(spielid=spielid)
	return execute_select_query(query)

def get_teilgenommene_turniere_pro_teilnehmer(teilnehmerid):
	query= 'select turnier.turnierid, turnier.name, turnier.jahr from turnierdetails as t inner join turnier on t.turnierid = turnier.turnierid where t.teilnehmerid = {teilnehmerid} group by t.turnierid;'.format(teilnehmerid=teilnehmerid)
	return execute_select_query(query)

def get_teilnehmerid(nickname):
	query = 'select teilnehmerid from teilnehmer where nickname = "{nickname}";'.format(nickname=nickname)
	return execute_select_query(query)

def get_teilnehmername(teilnehmerid):
	query = 'select name from teilnehmer where teilnehmerid={teilnehmerid};'.format(teilnehmerid=teilnehmerid)
	return execute_select_query(query)

def get_punkteliste(turnierid):
	query = 'select spiel.name, teilnehmer.name, "Runde: " || td.runde, "Platz: " || td.score from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid};'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_spielliste_pro_turnier(turnierid):
	query = 'select spiel.spielid, spiel.name from turnierdetails as td inner join turnier on td.turnierid = turnier.turnierid inner join spiel on td.spielid = spiel.spielid where td.turnierid = {turnierid} group by spiel.name;'.format(turnierid=turnierid)
	return execute_select_query(query)

def get_punkte_pro_spiel_pro_turnier(turnierid, spielid):
    gesamtergebnis = []

    runden = execute_select_query('SELECT DISTINCT(runde) FROM turnierdetails WHERE turnierid={turnierid} AND spielid={spielid};'.format(turnierid=turnierid, spielid=spielid))

    for runde in runden:
        scoretyp = execute_select_query('SELECT DISTINCT(scoretyp) FROM turnierdetails WHERE turnierid={turnierid} AND spielid={spielid} AND runde={runde};'.format(turnierid=turnierid, spielid=spielid, runde=runde[0]))

        query = 'SELECT spiel.name, teilnehmer.nickname, td.scoretyp, td.runde, td.score FROM turnierdetails AS td INNER JOIN teilnehmer ON td.teilnehmerid = teilnehmer.teilnehmerid INNER JOIN spiel ON td.spielid = spiel.spielid WHERE td.turnierid={turnierid} AND td.spielid={spielid} AND td.runde={runde} ORDER BY td.runde, td.score;'.format(turnierid=turnierid, spielid=spielid, runde=runde[0])
        gesamtergebnis.append(execute_select_query(query))

    return gesamtergebnis

def get_teilnehmerid_pro_turnier(turnierid):
	query = 'select teilnehmer from turnier where turnierid={turnierid}'.format(turnierid=turnierid)
	#query = 'select distinct(teilnehmerid) from turnierdetails where turnierid={turnierid};'.format(turnierid=turnierid)
	teilnehmerstr = execute_select_query(query) #teilnehmerstr [(None,)]
	#print("teilnehmerstr", teilnehmerstr)

	if teilnehmerstr[0][0] is None:
		return "None"
	else:
		return teilnehmerstr[0][0].split()

def get_runden_pro_spiel_pro_turnier(turnierid, spielid):
	query = 'select distinct(td.runde) from turnierdetails as td inner join teilnehmer on td.teilnehmerid = teilnehmer.teilnehmerid inner join spiel on td.spielid = spiel.spielid where td.turnierid={turnierid} and td.spielid={spielid} order by td.runde, td.score;'.format(turnierid=turnierid, spielid=spielid)
	return execute_select_query(query)

def get_turniere_pro_spiel(spielid):
	query = 'select distinct turnier.name, turnier.jahr from turnierdetails as v inner join turnier on v.turnierid = turnier.turnierid where v.spielid = {spielid};'.format(spielid=spielid)
	return execute_select_query(query)

def get_last_round(turnierid, spielid):
	query='select max(distinct(runde)) from turnierdetails where turnierid={turnierid} and spielid={spielid};'.format(turnierid=turnierid, spielid=spielid)
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