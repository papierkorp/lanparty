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
select "turnierdetailsid|turnierid|spielid|teilnehmerid|runde|ergebnistyp|ergebnis";

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
select "Laufendes Turnier Punkteliste: ";
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

- Gesamt
	+ sancho		4
	+ draham		4
	+ brandmeister	13
	+ tobse			7
	+ papierkorp	16
- CS
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
- Worms
	+ sancho		4
	+ draham		2
	+ brandmeister	6
	+ tobse			2
	+ papierkorp	8
- Worms Runde 1
	+ sancho		1
	+ draham		0
	+ brandmeister	5
	+ tobse			2
	+ papierkorp	3
- Worms Runde 2
	+ sancho		3
	+ draham		2
	+ brandmeister	1
	+ tobse			0
	+ papierkorp	5

## Chat GPT

Task:

Create a python Algorithm with following Requirements:

kills, the person with the most kills = 1. place
time, the person with the lowest secondes = 1. place


Total Points per Player = points of all games accumulated

Total Points per Game, 1. place = Number of Participants
Total Points per Game, 2. place = Number of Participants-2
Total Points per Game, 3. place = Number of Participants-3
...
Total Points per Game, last place = 0

You dont need to print the example Data.


This Data is available:

Format: ('Game', 'Player', 'calculation_type', 'round', 'score')

[
	[
		[
			('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), 
			('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), 
			('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), 
			('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), 
			('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)
		]
	], 
	[
		[
			('Trackmania', 'brandmeister', 'time', 1, 45), 
			('Trackmania', 'papierkorp', 'time', 1, 47), 
			('Trackmania', 'tobse', 'time', 1, 51), 
			('Trackmania', 'draham', 'time', 1, 77), 
			('Trackmania', 'sancho', 'time', 1, 93)
		]
	], 
	[
		[
			('Worms Armageddon', 'brandmeister', 'place', 1, 1), 
			('Worms Armageddon', 'papierkorp', 'place', 1, 2),
			('Worms Armageddon', 'tobse', 'place', 1, 3), 
			('Worms Armageddon', 'sancho', 'place', 1, 4), 
			('Worms Armageddon', 'draham', 'place', 1, 5)
		], 
		[
			('Worms Armageddon', 'papierkorp', 'place', 2, 1), 
			('Worms Armageddon', 'sancho', 'place', 2, 2), 
			('Worms Armageddon', 'draham', 'place', 2, 3), 
			('Worms Armageddon', 'brandmeister', 'place', 2, 4), 
			('Worms Armageddon', 'tobse', 'place', 2, 5)
		]
	]
] 


Example how the score should look (manually created):

- Total Points
	+ sancho		4 Points
	+ draham		4 Points
	+ brandmeister	13 Points
	+ tobse			7 Points
	+ papierkorp	16 Points
- CS Gesamt
	+ sancho		0 Points
	+ draham		1 Points
	+ brandmeister	2 Points
	+ tobse			3 Points
	+ papierkorp	5 Points
- CS Runde 1
	+ sancho		15 Kills
	+ draham		21 Kills
	+ brandmeister	30 Kills
	+ tobse			42 Kills
	+ papierkorp	45 Kills
- Trackmania Gesamt
	+ sancho		0 Points
	+ draham		1 Points
	+ brandmeister	5 Points
	+ tobse			2 Points
	+ papierkorp	3 Points
- Trackmania Runde 1
	+ sancho		93 Seconds
	+ draham		77 Seconds
	+ brandmeister	45 Seconds
	+ tobse			51 Seconds
	+ papierkorp	47 Seconds
- Worms Gesamt
	+ sancho		4 Points
	+ draham		2 Points
	+ brandmeister	6 Points
	+ tobse			2 Points
	+ papierkorp	8 Points
- Worms Runde 1
	+ sancho		4. Place
	+ draham		5. Place
	+ brandmeister	1. Place
	+ tobse			3. Place
	+ papierkorp	2. Place
- Worms Runde 2
	+ sancho		2. Place
	+ draham		3. Place
	+ brandmeister	4. Place
	+ tobse			5. Place
	+ papierkorp	1. Place
	

## ChatGPT2

Task:

Create a python Algorithm with following Requirements:

1. place (person with most kills) = get points according to the Number of Participants
2. place = get points according to the Number of Participants-2
3. place = get points according to the Number of Participants-3
...
Total Points per Game, last place (person with least kills) = gets 0 Points


Available Data:

Format: ('game', 'player', 'calculation_type', 'round', 'score')

[
	('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), 
	('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), 
	('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), 
	('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), 
	('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)
]


Example how the score should look (manually created):

- CS Total Points
	+ sancho		0 Points
	+ draham		1 Points
	+ brandmeister	2 Points
	+ tobse			3 Points
	+ papierkorp	5 Points
- CS Round1 Score
	+ sancho		15 Kills
	+ draham		21 Kills
	+ brandmeister	30 Kills
	+ tobse			42 Kills
	+ papierkorp	45 Kills