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

```sql
drop table if exists teilnehmer;
drop table if exists turnier;
drop table if exists spiel;
drop table if exists turnierdetails;
   
create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text unique);

create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr date default (strftime('%m-%Y')), teilnehmer text, sieger integer);

create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);

create table if not exists turnierdetails(turnierdetailsid integer primary key autoincrement, turnierid integer references turnier(turnierid), spielid integer references spiel(spielid), teilnehmerid integer references teilnehmer(teilnehmerid), runde integer, ergebnistyp text, ergebnis integer);
``` 

---------------------------------------------------------------------------
# TESTEINGABEN
---------------------------------------------------------------------------

```sql
insert into turnier(name) values("Lan Party");
insert into turnier(name) values("du musst hart sein wenn der Jungle weint");
insert into turnier(name) values("hype bock angriff");

insert into spiel(name, typ, maxspieler) values ("Counter Strike:Globale Offensive", "Dedicated Server", 10);
insert into spiel(name, typ, maxspieler) values ("Trackmania", "Ingame Server", 100);
insert into spiel(name, typ, maxspieler) values ("Worms Armageddon", "LAN", 4);
insert into spiel(name, typ, maxspieler) values ("GTA2", "LAN Client", 4);
insert into spiel(name, typ, maxspieler) values ("Quake Live", "Ingame Server", 100);
insert into spiel(name, typ, maxspieler) values ("Forts", "Ingame Server", 8);
insert into spiel(name, typ, maxspieler) values ("Mordhau", "Dedicated Server", 100);
insert into spiel(name, typ, maxspieler) values ("Minecraft", "Dedicated Server", 100);
insert into spiel(name, typ, maxspieler) values ("Scrap Mechanic", "Ingae Server", 100);
insert into spiel(name, typ, maxspieler) values ("Counter Strike: Source", "Dedicated Server", 10);
insert into spiel(name, typ, maxspieler) values ("The Hunter - Call of the Wild", "Ingame Server", 8);
insert into spiel(name, typ, maxspieler) values ("Tony Hawks Underground 2", "LAN Client", 8);
insert into spiel(name, typ, maxspieler) values ("Retrograde Arena", "LAN", 6);
insert into spiel(name, typ, maxspieler) values ("Ticket to Ride", "LAN", 5);
insert into spiel(name, typ, maxspieler) values ("Orcs must Die 2", "LAN", 2);
insert into spiel(name, typ, maxspieler) values ("Blobby Volley", "LAN", 2);

insert into teilnehmer(name, nickname) values("Markus", "papierkorp");
insert into teilnehmer(name, nickname) values("Tobi", "tobse");
insert into teilnehmer(name, nickname) values("Chris", "brandmeister");
insert into teilnehmer(name, nickname) values("Joahnn", "draham");
insert into teilnehmer(name, nickname) values("sancho", "sancho");
insert into teilnehmer(name, nickname) values("jones", "jones");
insert into teilnehmer(name, nickname) values("Felix", "spliffson");
insert into teilnehmer(name, nickname) values("Linus", "priestus");
insert into teilnehmer(name, nickname) values("Steve", "SteveO");
insert into teilnehmer(name, nickname) values("Dennis", "dizpy");
insert into teilnehmer(name, nickname) values("Daniel", "dan");
insert into teilnehmer(name, nickname) values("test", "test");
insert into teilnehmer(name, nickname) values("dummy", "dummy");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,1,1,1,45,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,1,2,1,42,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,1,3,1,30,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,1,4,1,21,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,1,5,1,15,"kills");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,2,1,1,47,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,2,2,1,51,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,2,3,1,45,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,2,4,1,77,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,2,5,1,93,"zeit");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,1,1,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,2,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,3,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,4,1,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,5,1,4,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,1,2,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,2,2,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,3,2,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,4,2,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (1,3,5,2,2,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,1,1,1,150,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,1,2,1,146,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,1,3,1,130,"kills");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,1,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,2,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,3,1,2,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,1,2,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,2,2,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,3,2,1,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,1,3,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,2,3,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,3,3,3,2,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,4,1,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,4,2,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,4,3,1,2,"platz");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,4,1,2,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,4,2,2,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (2,4,3,2,1,"platz");

--1=CSGO, 2=Trackmania, 3=Worms, 4=GTA2,,5=Quake Live,6=Forts
--7=Mordhau,8=Minecraft,9=Scrap Mechanic,10=Counter Strike: Source
--11=The Hunter - Call of the Wild,12=Tony Hawks Underground 2
--13=Retrograde Arena,14=Ticket to Ride

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,1,1,125,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,1,1,1,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,1,2,2,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,1,3,4,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,1,4,8,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,1,5,4,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,1,1,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,1,2,6,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,1,3,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,1,1,7777,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,1,1,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,1,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,1,1,18075,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,1,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,2,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,3,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,4,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,5,0,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,2,1,131,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,2,1,4,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,2,2,5,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,2,3,6,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,2,4,7,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,2,5,8,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,2,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,2,2,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,2,3,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,2,1,1500,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,2,1,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,2,1,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,2,1,21000,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,2,1,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,2,2,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,2,3,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,2,4,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,2,5,0,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,3,1,77,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,3,1,8,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,3,2,9,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,3,3,10,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,3,4,11,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,3,5,2,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,3,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,3,2,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,3,3,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,3,1,817,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,3,1,8,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,3,1,8,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,3,1,13459,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,3,1,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,3,2,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,3,3,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,3,4,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,3,5,1,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,4,1,120,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,4,1,3,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,4,2,3,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,4,3,2,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,4,4,1,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,4,5,2,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,4,1,10,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,4,2,11,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,4,3,11,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,4,1,354,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,4,1,9,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,4,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,4,1,1680,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,1,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,2,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,3,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,4,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,5,1,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,5,1,98,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,5,1,9,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,5,2,10,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,5,3,11,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,5,4,9,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,5,5,7,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,5,1,7,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,5,2,8,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,5,3,9,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,5,1,3333,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,5,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,5,1,6,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,5,1,8940,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,1,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,2,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,3,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,4,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,4,5,1,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,6,1,63,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,6,1,10,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,6,2,11,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,6,3,8,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,6,4,6,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,6,5,11,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,6,1,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,6,2,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,6,3,10,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,6,1,1498,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,6,1,10,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,6,1,9,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,6,1,14980,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,6,1,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,6,2,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,6,3,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,6,4,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,6,5,0,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,7,1,122,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,7,1,2,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,7,2,1,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,7,3,1,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,7,4,2,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,7,5,3,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,7,1,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,7,2,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,7,3,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,7,1,1500,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,7,1,3,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,7,1,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,7,1,34612,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,7,1,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,7,2,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,7,3,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,7,4,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,7,5,1,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,8,1,143,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,8,1,7,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,8,2,6,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,8,3,5,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,8,4,5,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,8,5,6,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,8,1,6,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,8,2,7,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,8,3,6,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,8,1,888,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,8,1,6,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,8,1,4,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,8,1,24698,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,8,1,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,8,2,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,8,3,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,8,4,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,8,5,0,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,9,1,86,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,9,1,11,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,9,2,8,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,9,3,7,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,9,4,10,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,9,5,9,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,9,1,9,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,9,2,10,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,9,3,8,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,9,1,1487,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,9,1,11,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,9,1,10,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,9,1,13947,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,1,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,2,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,3,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,4,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,1,5,1,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,10,1,103,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,10,1,5,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,10,2,4,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,10,3,3,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,10,4,3,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,10,5,5,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,10,1,8,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,10,2,1,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,10,3,2,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,10,1,947,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,10,1,5,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,10,1,7,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,10,1,36211,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,10,1,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,10,2,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,10,3,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,10,4,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,10,5,0,"pvp");

insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,7,11,1,111,"kills");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,11,1,6,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,11,2,7,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,11,3,9,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,11,4,4,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,2,11,5,10,"zeit");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,11,1,11,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,11,2,9,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,3,11,3,6,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,12,11,1,1587,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,13,11,1,7,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,14,11,1,11,"platz");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,15,11,1,32145,"Punkte");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,11,1,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,11,2,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,11,3,0,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,11,4,1,"pvp");
insert into turnierdetails(turnierid, spielid, teilnehmerid, runde, ergebnis, ergebnistyp) values (3,16,11,5,1,"pvp");
```


---------------------------------------------------------------------------
# Test SQL-Statements
---------------------------------------------------------------------------

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