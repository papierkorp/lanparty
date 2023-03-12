Tabelle teilnehmer
Felder: teilnehmerid (int), name (text), nickname (text)

Tabelle turnier
Felder: turnierid (int), name (text), jahr (date), teilnehmer(TeilnehmerID)

Tabelle spiel
Felder: spielid (int), name (text), typ (text)(Dedicated Server, Ingame Server, LAN...), maxspieler (int)

Tabelle turnierdetails
Felder: turnierdetailsid (int), turnierid (turnierid), spielid (spielid), teilnehmerid (teilnehmerid), runde (int), spieltyp (text), ergebnistyp (text), ergebnis (int)