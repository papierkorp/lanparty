drop table if exists teilnehmer;
drop table if exists turnier;
drop table if exists spiel;
drop table if exists turnierdetails;
   
create table if not exists teilnehmer(teilnehmerid integer primary key autoincrement, name text, nickname text unique);
create table if not exists turnier(turnierid integer primary key autoincrement, name text, jahr date default (strftime('%m-%Y')), teilnehmer text, sieger integer);
create table if not exists spiel(spielid integer primary key autoincrement, name text, typ text, maxspieler integer);
create table if not exists turnierdetails(turnierdetailsid integer primary key autoincrement, turnierid integer references turnier(turnierid), spielid integer references spiel(spielid), teilnehmerid integer references teilnehmer(teilnehmerid), runde integer, scoretyp text, score integer, result integer);