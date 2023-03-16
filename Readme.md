Kleines privates Flask Projekt.
Eine Webseite die für ein LAN-Turnier herhalten muss.

Projekt installieren:
```
mkdir lan
cd lan
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Webseite lokal starten:
```
cd lan
FLASK_APP=lan.py #Environment Variable setzen
venv\Scripts\activate
flask run
```