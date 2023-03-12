from collections import defaultdict

def Ergebnisberechnung(punkteliste):
    ordnung = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'Punkte': False,
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

            #print("    punkte_runde:", sorted(punkte_runde.items(), key=lambda x: x[1], reverse=True))
        #print("  punkte_game:", sorted(punkte_game.items(), key=lambda x: x[1], reverse=True))
    #print("\npunkte_gesamt:", sorted(punkte_gesamt.items(), key=lambda x: x[1], reverse=True))
    return(sorted(punkte_gesamt.items(), key=lambda x: x[1], reverse=True))
