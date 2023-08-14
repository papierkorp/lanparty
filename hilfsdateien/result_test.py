#Online Python: https://www.programiz.com/python-programming/online-compiler/
from collections import defaultdict

# Zielausgabe

# - Total
# 	+ sancho		2 = sum of all games
# 	+ draham		3 = sum of all games
# 	+ brandmeister	10 = sum of all games
# 	+ tobse			6 = sum of all games
# 	+ papierkorp	13 = sum of all games
# - Counter Strike:Globale Offensive
# 	+ sancho		(15 kills) => 0 punkte
# 	+ draham		(21 kills) => 1 punkte
# 	+ brandmeister	(30 kills) => 2 punkte
# 	+ tobse			(42 kills) => 3 punkte
# 	+ papierkorp	(45 kills) => 5 punkte
# - Trackmania
# 	+ sancho		(93 sec) => 0 punkte
# 	+ draham		(77 sec) => 1 punkte
# 	+ brandmeister	(45 sec) => 5 punkte
# 	+ tobse			(51 sec) => 2 punkte
# 	+ papierkorp	(47 sec) => 3 punkte
# - Worms Armageddon Gesamt
# 	+ sancho		(sum_of_all_rounds=4) => 2 punkte
# 	+ draham		(sum_of_all_rounds=2) => 1 punkte
# 	+ brandmeister	(sum_of_all_rounds=6) => 3 punkte
# 	+ tobse			(sum_of_all_rounds=2) => 1 punkte
# 	+ papierkorp	(sum_of_all_rounds=8) => 5 punkte
# - Worms Armageddon Runde 1
# 	+ sancho		(4 platz) => 1 punkte
# 	+ draham		(5 platz) => 0 punkte
# 	+ brandmeister	(1 platz) => 5 punkte
# 	+ tobse			(3 platz) => 2 punkte
# 	+ papierkorp	(2 platz) => 3 punkte
# - Worms Armageddon Runde 2
# 	+ sancho		(2 platz) => 3 punkte
# 	+ draham		(3 platz) => 2 punkte
# 	+ brandmeister	(4 platz) => 1 punkte
# 	+ tobse			(5 platz) => 0 punkte
# 	+ papierkorp	(1 platz) => 5 punkte


# Data wird übergeben
data = [[[('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)]], [[('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)]], [[('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 'platz', 1, 5)], [('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)]]]

''' 
[
	[
		[
			('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)
		]
	], 
	[
		[
			('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)
		]
	], 
	[
		[
			('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 'platz', 1, 5)
		], 
		[
			('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)
		]
	]
]
'''

def result(data):
	print("data", data)
	score_type = {
		'kills': True,
		'zeit': False,
		'platz': False,
		'pvp': False,
		'punkte': False,
	}
	punkte_gesamt = defaultdict(int)

	for game in data:
		punkte_game = defaultdict(int)
		gameName = game[0][0][0]
		total_rounds = len(game)
		for game_round in game:
			current_round = game_round[0][3]
			print("\ngame: %s, total rounds: %s, current round: %s\n" % (gameName, total_rounds, current_round))
			runde_sortiert = sorted(game_round, key=lambda x: x[4], reverse=score_type[game_round[0][2]])
			punkte_runde = {x[1]: len(runde_sortiert) - (i + 1 if i else 0) for i, x in enumerate(runde_sortiert)}
			print("Punkte_runde", punkte_runde)

result(data)
















# Legacy
print("--------------------------------------------------------------")
def auswertung_legacy(data):
    ordnung = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'punkte': False,
    }

    punkte_gesamt = defaultdict(int)

    for spiel in data:
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

#auswertung_legacy(data)