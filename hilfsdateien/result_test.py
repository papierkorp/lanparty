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

data = [[[('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)]], [[('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)]], [[('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 'platz', 1, 5)], [('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)]]]

def Ergebnisberechnung_gesamt(data, returnType="total"):
    #data = [[[('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)]], [[('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)]], [[('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 'platz', 1, 5)], [('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)]]]
    print("data", data)
    points_total = {}
    returnType_perGame = data
    score_type_list = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'punkte': False,
    }
    

    for game in data:
        points_per_game = {}
        for game_round in game:
            total_players = len(game_round)
            current_round = game_round[0][3]
            score_type = game_round[0][2]
            gameName = game[0][0][0]
            total_rounds = len(game)
            print("\ngame: %s, total players: %s, total rounds: %s, current round: %s, score type: %s" % (gameName, total_players, total_rounds, current_round, score_type))

            round_sorted = sorted(game_round, key=lambda x: x[4], reverse=score_type_list[score_type])
            round_sorted_nicknames_and_scores = [(nickname, score) for _, nickname, _, _, score in round_sorted]
            points_per_game[current_round] = evaluate_points(data = round_sorted_nicknames_and_scores)
            print("round_sorted_nicknames_and_scores", round_sorted_nicknames_and_scores)
            print("points_per_game", points_per_game)
            print("game_round", game_round)
            for player_tuple in game_round:
                round_number = player_tuple[3]
                player_nickname = player_tuple[1]
        
                if round_number in points_per_game:
                    pointstemp = points_per_game[round_number].get(player_nickname, 0)
                    player_tuple = player_tuple + (pointstemp,)
                    print("player_tuple", player_tuple)

                    for outer_idx, outer_game_round in enumerate(returnType_perGame):
                        for inner_idx, original_game_round in enumerate(outer_game_round):
                            for original_player_tuple_idx, original_player_tuple in enumerate(original_game_round):
                                if (
                                    original_player_tuple[0] == gameName
                                    and original_player_tuple[1] == player_nickname
                                    and original_player_tuple[3] == round_number
                                ):
                                    updated_tuple = (*original_player_tuple, pointstemp)
                                    returnType_perGame[outer_idx][inner_idx][original_player_tuple_idx] = updated_tuple




        total_points_per_game = {}
        for count, data in points_per_game.items():
            for player, point in data.items():
                if player in total_points_per_game:
                    total_points_per_game[player] += point
                else:
                    total_points_per_game[player] = point
        sorted_total_points_per_game = sorted(total_points_per_game.items(), key=lambda item: item[1], reverse=True)

        total_points_per_game = evaluate_points(data = sorted_total_points_per_game)
        print("total_points_per_game",total_points_per_game)
        points_total[gameName] = total_points_per_game
        


    total_points_per_player = {}
    for data in points_total.values():
        for player, points in data.items():
            if player in total_points_per_player:
                total_points_per_player[player] += points
            else:
                total_points_per_player[player] = points
    sorted_total_points_per_player = dict(sorted(total_points_per_player.items(), key=lambda item: item[1], reverse=True))
    print("Total points per player:\n", sorted_total_points_per_player)
    
    if returnType=="perGame":
        return returnType_perGame
    else:
        return sorted_total_points_per_player



def evaluate_points(data):
    #data = [('papierkorp', 8), ('brandmeister', 6), ('sancho', 4), ('tobse', 2), ('draham', 2)]
    points = {}
    last_score = None
    same_score_count = 0
    total_players = len(data)
    
    for count, playertuple in enumerate(data):
        player=playertuple[0]
        score=playertuple[1]
        if last_score == None:
            points[player] = total_players
        elif last_score == score:
            same_score_count += 1
            points[player] = total_players - (count - same_score_count + 1 if count else 0)
        else:
            same_score_count = 0
            points[player] = total_players - (count + 1 if count else 0)

        last_score = score
        last_player = player
    return points


print("\n\n\n", Ergebnisberechnung_gesamt(data, "perGame"))

points_per_game = {1: {'brandmeister': 5, 'papierkorp': 3, 'tobse': 2, 'sancho': 1, 'draham': 0}}

game_round = [
    ('Worms Armageddon', 'brandmeister', 'platz', 1, 1),
    ('Worms Armageddon', 'papierkorp', 'platz', 1, 2),
    ('Worms Armageddon', 'tobse', 'platz', 1, 3),
    ('Worms Armageddon', 'sancho', 'platz', 1, 4),
    ('Worms Armageddon', 'draham', 'platz', 1, 5)
]

for player_tuple in game_round:
    game_round_number = player_tuple[3]
    player_nickname = player_tuple[1]
    
    if game_round_number in points_per_game:
        points = points_per_game[game_round_number].get(player_nickname, 0)
        player_tuple = player_tuple + (points,)
    