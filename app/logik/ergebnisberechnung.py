from collections import defaultdict

def Ergebnisberechnung_gesamt(punkteliste):
    ordnung = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'punkte': False,
    }

    punkte_gesamt = defaultdict(int)

    for spiel in punkteliste:
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
