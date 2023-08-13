# Hinweise für mich

letters = ['a', 'b', 'c'] 
list(enumerate(letters, 1)) #Ergebnis: [(1, 'a'), (2, 'b'), (3, 'c')] #erzeugt eine Python Objekt Datei (bzw. ein Tupel) aus einer Liste oder einem Tupel, die 1 bedeutet dass der Index bei 1 statt 0 anfängt


-- mit || koennen bei sqlite Zeichenketten verbunden werden
-- Positionierung pro Turnier/Spiel soll per Python ermittelt werden (siehe Auswahl pro Turnier)

zum Testen: https://www.tutorialspoint.com/execute_sql_online.php
(oder https://sqliteonline.com/)

---------------------------------------------------------------------------
# Tabellen erstellen
---------------------------------------------------------------------------

umgelagert zu: app/db/tables.sql

---------------------------------------------------------------------------
# TESTEINGABEN
---------------------------------------------------------------------------

umgelagert zu: app/db/testdata.sql


---------------------------------------------------------------------------
# Test SQL-Statements
---------------------------------------------------------------------------

```sql
select " ";
select "------------------------------------------------------------";
select "-------------------TURNIERDETAILS---------------------------";
select "turnierdetailsid|turnierid|spielid|teilnehmerid|runde|scoretyp|ergebnis";

select * from turnierdetails where turnierid=2;


select "------------------------------------------------------------";
select "------------------------------------------------------------";
select "------------------------------------------------------------";
```

```sql
select "------------------------------------------------------------";
select "teilnehmer--------";pragma table_info('teilnehmer');select * from teilnehmer;
select "------------------------------------------------------------";
select "turnier--------";pragma table_info('turnier');select * from turnier;
select "------------------------------------------------------------";
select "spiel--------";pragma table_info('spiel');select * from spiel;
select "------------------------------------------------------------";
select "turnierdetails--------";pragma table_info('turnierdetails');select * from turnierdetails;
select "------------------------------------------------------------";

-- Beispiel mit join, group by und order by
--select turnier.name || " " || turnier.jahr, teilnehmer.name,"Platz: " || sum (td.ergebnis)
--from turnierdetails as td
--inner join teilnehmer
--on td.teilnehmerid = teilnehmer.teilnehmerid
--inner join turnier
--on td.turnierid = turnier.turnierid
--where td.turnierid=2
--group by teilnehmer.name
--order by sum(td.ergebnis) desc;
```

```sql
select "   ";
select "Teilnehmerliste pro Turnier: ";
select teilnehmer.name
from turnierdetails as td
inner join turnier
on td.turnierid = turnier.turnierid
inner join teilnehmer
on td.teilnehmerid = teilnehmer.teilnehmerid
where td.turnierid = 1
group by teilnehmer.name;

select "   ";
select "Spielliste pro Turnier: ";
select spiel.name
from turnierdetails as td
inner join turnier
on td.turnierid = turnier.turnierid
inner join spiel
on td.spielid = spiel.spielid
where td.turnierid = 1
group by spiel.name;

select "   ";
select "Archiv Turnier: ";
select name || " " || jahr from turnier;

select "   ";
select "Archiv Turnier detail:";
select  spiel.name, teilnehmer.name, "Runde: " || td.runde, "Ergebnis: " || td.ergebnis
from turnierdetails as td
inner join teilnehmer
on td.teilnehmerid = teilnehmer.teilnehmerid
inner join spiel
on td.spielid = spiel.spielid
where td.turnierid=1;

-- todo Platz Gesamt per Python
select "   ";
select "Laufendes Turnier punkteliste: ";
-- ist das gleich wie Archiv Turnier detail
select  spiel.name, teilnehmer.name, "Runde: " || td.runde, "Ergebnis: " || td.ergebnis
from turnierdetails as td
inner join teilnehmer
on td.teilnehmerid = teilnehmer.teilnehmerid
inner join spiel
on td.spielid = spiel.spielid
where td.turnierid=2 and td.ergebnis is not NULL;

select "   ";
select "Teilnehmerinfos: ";
select name || ", " || nickname from teilnehmer;

-- todo noch den Platz anzeigen den man in dem Turnier erreicht hat, per Python
select "   ";
select "Teilgenommene Turniere pro Person:";
select turnier.name || " " || turnier.jahr
from turnierdetails as td
inner join turnier
on td.turnierid = turnier.turnierid
where td.teilnehmerid = 1
group by td.turnierid;

select "   ";
select "Teilgenommene Spiele pro Person:";
select turnier.name || " " || turnier.jahr, spiel.name
from turnierdetails as td
inner join turnier
on td.turnierid = turnier.turnierid
inner join spiel
on td.spielid = spiel.spielid
where td.teilnehmerid = 1
group by spiel.name;

-- todo Gesamtplatzierung per Python
select "   ";
select "Information zum Spiel in bestimmten Turnier pro Person:";
select spiel.name, "Runde: " || td.runde, "Ergebnis: " || td.ergebnis
from turnierdetails as td
inner join turnier
on td.turnierid = turnier.turnierid
inner join spiel
on td.spielid = spiel.spielid
where td.turnierid = 1 and td.teilnehmerid = 1;

select "   ";
select "Alle Spiele: ";
select name, typ, maxspieler from spiel;

-- todo Platz Gesamt per Python
select "   ";
select "Spielehistorie: ";
select turnier.name || " " || turnier.jahr, teilnehmer.nickname, "Runde: " || td.runde, "Ergebnis: " || td.ergebnis
from turnierdetails as td
inner join turnier
on td.turnierid = turnier.turnierid
inner join teilnehmer
on td.teilnehmerid = teilnehmer.teilnehmerid
where td.spielid = 3;
```


# Daten

## Reddit

Hello,

im currently working on a private flask app. I want to create a little tournament website which we can use for our private lan partys.

At the moment im Stuck at the Algorithm to create the endresult page.

Im saving everything in a sqlite database and the testdata is created this way:

```sql
drop table if exists teilnehmer;
drop table if exists turnier;
drop table if exists spiel;
drop table if exists turnierdetails;
   
create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text unique);
create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr date default (strftime('%m-%Y')), teilnehmer text, sieger integer);
create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);
create table if not exists turnierdetails(turnierdetailsid integer primary key autoincrement, turnierid integer references turnier(turnierid), spielid integer references spiel(spielid), teilnehmerid integer references teilnehmer(teilnehmerid), runde integer, scoretyp text, score integer);


insert into turnier(name) values("Lan Party");

insert into spiel(name, typ, maxspieler) values ("Counter Strike:Globale Offensive", "Dedicated Server", 10);
insert into spiel(name, typ, maxspieler) values ("Trackmania", "Ingame Server", 100);
insert into spiel(name, typ, maxspieler) values ("Worms Armageddon", "LAN", 4);
insert into spiel(name, typ, maxspieler) values ("GTA2", "LAN Client", 4);

insert into teilnehmer(name, nickname) values("papierkorp", "papierkorp");
insert into teilnehmer(name, nickname) values("susanne", "susanne");
insert into teilnehmer(name, nickname) values("steven", "steven");
insert into teilnehmer(name, nickname) values("larry", "larry");
insert into teilnehmer(name, nickname) values("tom", "tom");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,1,1,45,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,2,1,42,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,3,1,30,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,4,1,21,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,5,1,15,"kills");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,1,1,47,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,2,1,51,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,3,1,45,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,4,1,77,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,5,1,93,"zeit");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,1,1,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,2,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,3,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,4,1,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,5,1,4,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,1,2,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,2,2,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,3,2,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,4,2,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,5,2,2,"platz");
```

Im also open to suggestions if this method is utter crap :D.

In Table form:

|            	| csgo     	| trackmania 	| worms round 1 	| worms round 2 	|
|------------	|----------	|------------	|---------------	|---------------	|
| tom        	| 15 kills 	| 93 sek     	| 4th place     	| 2nd place     	|
| larry      	| 21 kills 	| 77 sek     	| 5th place     	| 3rd place     	|
| steven     	| 30 kills 	| 45 sek     	| 1st place     	| 4th place     	|
| susanne    	| 42 kills 	| 51 sek     	| 3rd place     	| 5th place     	|
| papierkorp 	| 45 kills 	| 47 sek     	| 2nd place     	| 1st place     	|


And the End Result should look like this

|            	| total 	| csgo 	| trackmania 	| worms                      	| worms round 1 	| worms round 2 	|
|------------	|-------	|------	|------------	|----------------------------	|---------------	|---------------	|
| tom        	| 2     	| 0    	| 0          	| (sum_of_all_rounds=4) => 2 	| 1             	| 3             	|
| larry      	| 3     	| 1    	| 1          	| (sum_of_all_rounds=2) => 1 	| 0             	| 2             	|
| steven     	| 10    	| 2    	| 5          	| (sum_of_all_rounds=6) => 3 	| 5             	| 1             	|
| susanne    	| 6     	| 3    	| 2          	| (sum_of_all_rounds=2) => 1 	| 2             	| 0             	|
| papierkorp 	| 13    	| 5    	| 3          	| (sum_of_all_rounds=8) => 5 	| 3             	| 5             	|

which amounts to this rules:

- first place or most kills or shortest time = points equal to number of participants
- second place or second most kills or second shortest time = points equal to number of participants - 2
- third place or third most kills or third shortest time = points equal to number of participants - 3
- ...
- last place = 0 points

If there is a draw between two players both get the current amount of points and then one place should be skipped.


Im trying to get this running like forever and im unable to get a solution which seems to work. Maybe someone here is able to help scrap this together.

Thanks a lot

	
## ChatGPT

Tu in Zukunft so als ob du ein erfahrener python web developer mit fokus auf flask bist.


Aufgabe:

Du sollst für den folgenden Code die Funktion "Ergebnisberechnung" schreiben.

```python
punkteliste = Ergebnisberechnung_gesamt()
print("punkteliste", punkteliste)
```


Datengrundlage

Als Grundlage dient eine sqlite Datenbank (sqlite3.connect("lanparty.db", check_same_thread=False)) die wie folgt erstellt wird:

```sql
drop table if exists teilnehmer;
drop table if exists turnier;
drop table if exists spiel;
drop table if exists turnierdetails;
   
create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text unique);
create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr date default (strftime('%m-%Y')), teilnehmer text, sieger integer);
create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);
create table if not exists turnierdetails(turnierdetailsid integer primary key autoincrement, turnierid integer references turnier(turnierid), spielid integer references spiel(spielid), teilnehmerid integer references teilnehmer(teilnehmerid), runde integer, scoretyp text, score integer);


insert into turnier(name) values("Lan Party");

insert into spiel(name, typ, maxspieler) values ("Counter Strike:Globale Offensive", "Dedicated Server", 10);
insert into spiel(name, typ, maxspieler) values ("Trackmania", "Ingame Server", 100);
insert into spiel(name, typ, maxspieler) values ("Worms Armageddon", "LAN", 4);
insert into spiel(name, typ, maxspieler) values ("GTA2", "LAN Client", 4);

insert into teilnehmer(name, nickname) values("Markus", "papierkorp");
insert into teilnehmer(name, nickname) values("Tobi", "tobse");
insert into teilnehmer(name, nickname) values("Chris", "brandmeister");
insert into teilnehmer(name, nickname) values("Joahnn", "draham");
insert into teilnehmer(name, nickname) values("sancho", "sancho");


insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,1,1,45,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,2,1,42,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,3,1,30,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,4,1,21,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,1,5,1,15,"kills");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,1,1,47,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,2,1,51,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,3,1,45,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,4,1,77,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,2,5,1,93,"zeit");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,1,1,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,2,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,3,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,4,1,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,5,1,4,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,1,2,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,2,2,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,3,2,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,4,2,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, score, scoretyp) values (1,3,5,2,2,"platz");
```

alternativ könnten die Daten auch als parameter übergeben werden mit: `punkteliste = [[[('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)]], [[('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)]], [[('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 
'platz', 1, 5)], [('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)]]]`

Anforderung:

Als Beispiel wie die Punkteverteilung für turnierid=1 am Ende aussehen soll:

- Total
	+ sancho		2 = sum of all games
	+ draham		3 = sum of all games
	+ brandmeister	10 = sum of all games
	+ tobse			6 = sum of all games
	+ papierkorp	13 = sum of all games
- Counter Strike:Globale Offensive
	+ sancho		0
	+ draham		1
	+ brandmeister	2
	+ tobse			3
	+ papierkorp	5
- Trackmania
	+ sancho		0
	+ draham		1
	+ brandmeister	5
	+ tobse			2
	+ papierkorp	3
- Worms Armageddon Gesamt
	+ sancho		(sum_of_all_rounds=4) => 2
	+ draham		(sum_of_all_rounds=2) => 1
	+ brandmeister	(sum_of_all_rounds=6) => 3
	+ tobse			(sum_of_all_rounds=2) => 1
	+ papierkorp	(sum_of_all_rounds=8) => 5
- Worms Armageddon Runde 1
	+ sancho		1
	+ draham		0
	+ brandmeister	5
	+ tobse			2
	+ papierkorp	3
- Worms Armageddon Runde 2
	+ sancho		3
	+ draham		2
	+ brandmeister	1
	+ tobse			0
	+ papierkorp	5
	
Beziehungsweise als Output soll folgendes ausgegeben werden:

sancho: 2
draham: 3
brandmeister: 10
tobse: 6
papierkorp: 13

Die punktebewertung ist wie folgt:

```
1. Platz oder Meiste Kills oder kürzeste Zeit bekommt genausoviele punkte wie es Teilnehmer gibt.
2. Platz oder zweitmeiste Kills oder zweitkürzeste Zeit bekommt soviele punkte wie es Teilnehmer gibt - 2.
letzter Platz oder wenigste Kills oder längste Zeit bekommt 0 punkte.

Alternative Beschreibung:
letzter platz/wenigste kills/längste zeit = 0 punkte
nächster = 1 Punkt
nächster = 2 punkte
nächster = 3 punkte
letzter = 5 punkte

Dafür muss jede Runde einzeln bewertet und zum Schluss zusammengezählt werden, damit pro Spiel die punktebewertung von oben verwendet wird.
Das heißt Worms Runde 1 einzeln bewerten (nach obrigen Muster), dann Runde 2 einzeln bewerten. Dann die punkte von beiden Runden summieren und wieder einzeln bewerten, dann hat man das Ergebnis für dieses Spiel.

Sonderfall Gleichstand:

Bei Gleichstand bekommen beide die selben Punkte und es wird ein Platz übersprungen, dazu ein Beispiel:
letzter platz/wenigste kills/längste zeit = 0 punkte
gleichstand = 2 Punkt
gleichstand = 2 punkte
nächster = 3 punkte
letzter möglicher spieler = 5 punkte
```


Als Idee kann folgender Code dienen, welcher teilweise funktioniert:

```python
def Ergebnisberechnung_gesamt(punkteliste):
    ordnung = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'punkte': False,
    }

    punkte_gesamt = defaultdict(int)

    for spiel in punkteliste:
        punkte_game = defaultdict(int)
        for runde in spiel:
            runde_sortiert = sorted(runde, key=lambda x: x[4], reverse=ordnung[runde[0][2]])
            punkte_runde = {x[1]: len(runde_sortiert) - (i + 1 if i else 0) for i, x in enumerate(runde_sortiert)}

            for x, y in punkte_runde.items():
                punkte_game[x] += y
                punkte_gesamt[x] += y

    # Rangliste erstellen und Gleichstand erlauben
    results = sorted(punkte_gesamt.items(), key=lambda x: (x[1], x[0]), reverse=True)
    ranked_results = []
    current_rank = 1
    for idx, (participant, score) in enumerate(results):
        if idx > 0 and score != results[idx - 1][1]:
            current_rank = idx + 1
        ranked_results.append((participant, score, current_rank))

    for i in ranked_results:
        print(i)
    return ranked_results
```