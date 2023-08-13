Tabelle teilnehmer
Felder: teilnehmerid (int), name (text), nickname (text)

Tabelle turnier
Felder: turnierid (int), name (text), jahr (date), teilnehmer(TeilnehmerID)

Tabelle spiel
Felder: spielid (int), name (text), typ (text)(Dedicated Server, Ingame Server, LAN...), maxspieler (int)

Tabelle turnierdetails
Felder: turnierdetailsid (int), turnierid (turnierid), spielid (spielid), teilnehmerid (teilnehmerid), runde (int), scoretyp (text), ergebnis (int)


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
#turnierdetails
#--turnierdetailsid(int)
#--turnierid(int)
#--spielid(int)
#--teilnehmerid(int)
#--runde(int)
#--scoretyp(text)
#--ergebnis(string)