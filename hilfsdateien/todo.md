# havetodo
- Turnier - Übersicht - xxx - Spiel - Turnierbaum erstellen
- Turnierdetails - punkteliste - Gesamtpunkteauswertung (Ergebnisberechnung): zwei spieler mit selbem ergebnis werden noch nicht berücksichtigt
- Turnierdetails - punkteliste - Gesamtpunkteauswertung (Ergebnisberechnung): "punkte" "pvp" usw... einbauen

# wanttodo

- Allgemein
  - route File refactore lul
  - Tests
  - Variablen Namen / Funktionsnamen - auf englisch oder deutsch festlegen und kein mix
  - Logit aus routes.py rausnehmen?
- Turnier
  - Turnier - Übersicht - xxx -punkteliste pro Spiel
  - Turnier - Übersicht - xxx - Platzierung
  - Turnier löschen
  - Turnier bearbeiten (Teilnehmer hinzu oder weg)
  - Turnier - neu - Spielauswahl hinzufügen?
  - scoretyp wird mehrmals definiert
  - Turnier - Übersicht: Rundenausgabe pro Spiel überarbeiten
  - Ergebnis als json/yaml übergeben
  - Turnier - Übersicht - xxx - Runde löschen, bei Ergebnisausgabe gibts noch nen Hack, wenn eine Runde in der Mitte gelöscht wird, sind maximal 5 Runden unterschied zulässig...
  - Turnier - Übersicht - xxx - Runde hinzufügen, evtl. statt letzte Runde + 1, raussuchen ob es leere Runden dazwischen gibt? (spricht eigt. gegen Integrität höhö)
- Teilnehmer
  - Teilnehmer - xxx - Turniernamelink
  - Teilnehmer bearbeiten (Name + Nickname ändern)
  - Bei Teilnehmerübersicht - Platzierung je Turnier hinzufügen
  - Teilnehmerübersicht: Teilgenommene Spiele + zugehöriges Turnier + Platzierung anzeigen
- Spiele
  - Spiele - Übersicht - Filter
  - Spiel bearbeiten (Details ändern)
  - Spiel hinzufügen - Typ Select
- Style
  - Bootstrap verwenden
  - Tabellen Bibliothek
  - Navigation von reinem CSS weg und ne Python Lösung finden? (ist halt schon witzig mit reinem css :D)
  - irgendwas für Startseite einfallen lassen
  - disabled form style (ergebnis.html > forms.css > #myForm_edit .form_disabled )
  - Turnier - xxx Game hinzufügen/löschen Form überarbeiten
- Datenbank
  - DB - Tabelle Turnier - das Feld Teilnehmer in Sieger umbennenen - teilnehmer spalte in turnier Tabelle nötig?
  - funktion edit_ergebnis = spielid und turnierid durch namen ersetzen
  - funktion get_punkte_pro_spiel_pro_turnier = nach name sortieren..
  - DB aufsplitten in mehrere Dateien?
  - werden noch alle query benötigt?
  - wenn db leer ist, hagelt es fehlermeldungen (weil die querys nicht ausgeführt werden können)
Optimierungen
  - Ergebnis bearbeiten - nur für Änderungen eine Abfrage ausführen und nicht für alles
  - Ergebnis bearbeiten - spielid übergeben und nicht einzeln abfragen