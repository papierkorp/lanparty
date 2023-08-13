Kleines privates Flask Projekt.
Eine Webseite die für ein LAN-Turnier herhalten muss.

# Windows

Projekt installieren:
```
mkdir lan
cd lan
python3 -m venv venv
venv\Scripts\activate
pip install -r ./hilfsdateien/requirements.txt
```

Webseite lokal starten:
```
cd lan
#env Variablen sollten in der /.flaskenv Datei gespeichert sein, ansonsten env Variablen manuell setzen
FLASK_APP=lan.py #Environment Variable setzen
FLASK_DEBUG=1 #Environment Variable setzen
venv\Scripts\activate
flask run
```

# Linux

Projekt installieren:
```
mkdir lan
cd lan
python3 -m venv venv
source venv/bin/activate
pip install -r ./hilfsdateien/requirements.txt
```

Webseite lokal starten:
```
cd lan
#env Variablen sollten in der /.flaskenv Datei gespeichert sein, ansonsten env Variablen manuell setzen
export FLASK_APP=lan.py #Environment Variable setzen
export FLASK_DEBUG=1 #Environment Variable setzen
source venv/bin/activate
flask run
```