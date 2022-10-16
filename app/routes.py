from app import app

@app.route('/')
@app.route('/index')
def index():
	user={"username": "papierkorp"}
	return render_template('index.html', user=user)

@app.route('/turnier')
def turnier():
	return "Turnier!"

@app.route('/teilnehmer')
def teilnehmer():
	return "Teilnehmer!"


@app.route('/Spiele')
def spiele():
	return "Spiele!"

