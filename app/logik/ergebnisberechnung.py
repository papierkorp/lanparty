from collections import defaultdict

#punkteliste=
#[
#    [
#        [
#            ('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), 
#            ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), 
#            ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), 
#            ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), 
#            ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)
#        ]
#    ], 
#    [
#        [
#            ('Trackmania', 'brandmeister', 'zeit', 1, 45), 
#            ('Trackmania', 'papierkorp', 'zeit', 1, 47), 
#            ('Trackmania', 'tobse', 'zeit', 1, 51), 
#            ('Trackmania', 'draham', 'zeit', 1, 77), 
#            ('Trackmania', 'sancho', 'zeit', 1, 93)
#        ]
#    ], 
#    [
#        [
#            ('Worms Armageddon', 'brandmeister', 'platz', 1, 1), 
#            ('Worms Armageddon', 'papierkorp', 'platz', 1, 2),
#            ('Worms Armageddon', 'tobse', 'platz', 1, 3), 
#            ('Worms Armageddon', 'sancho', 'platz', 1, 4), 
#            ('Worms Armageddon', 'draham', 'platz', 1, 5)
#        ], 
#        [
#            ('Worms Armageddon', 'papierkorp', 'platz', 2, 1), 
#            ('Worms Armageddon', 'sancho', 'platz', 2, 2), 
#            ('Worms Armageddon', 'draham', 'platz', 2, 3), 
#            ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), 
#            ('Worms Armageddon', 'tobse', 'platz', 2, 5)
#        ]
#    ]
#]

def Ergebnisberechnung(punkteliste):
    ordnung = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'Punkte': False,
    }
    print("punkteliste", punkteliste)
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
