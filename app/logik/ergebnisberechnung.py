from collections import defaultdict
import copy

data = [[[('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)]], [[('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)]], [[('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 'platz', 1, 5)], [('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)]]]

def Ergebnisberechnung_gesamt(data, returnType="total"):
    #data = [[[('Counter Strike:Globale Offensive', 'sancho', 'kills', 1, 15), ('Counter Strike:Globale Offensive', 'draham', 'kills', 1, 21), ('Counter Strike:Globale Offensive', 'brandmeister', 'kills', 1, 30), ('Counter Strike:Globale Offensive', 'tobse', 'kills', 1, 42), ('Counter Strike:Globale Offensive', 'papierkorp', 'kills', 1, 45)]], [[('Trackmania', 'brandmeister', 'zeit', 1, 45), ('Trackmania', 'papierkorp', 'zeit', 1, 47), ('Trackmania', 'tobse', 'zeit', 1, 51), ('Trackmania', 'draham', 'zeit', 1, 77), ('Trackmania', 'sancho', 'zeit', 1, 93)]], [[('Worms Armageddon', 'brandmeister', 'platz', 1, 1), ('Worms Armageddon', 'papierkorp', 'platz', 1, 2), ('Worms Armageddon', 'tobse', 'platz', 1, 3), ('Worms Armageddon', 'sancho', 'platz', 1, 4), ('Worms Armageddon', 'draham', 'platz', 1, 5)], [('Worms Armageddon', 'papierkorp', 'platz', 2, 1), ('Worms Armageddon', 'sancho', 'platz', 2, 2), ('Worms Armageddon', 'draham', 'platz', 2, 3), ('Worms Armageddon', 'brandmeister', 'platz', 2, 4), ('Worms Armageddon', 'tobse', 'platz', 2, 5)]]]
    print("=============================================")
    print("ERGEBNISBERECHNUNG")
    print("=============================================")
    print("data", data)
    points_total = {}
    returnType_perGame = copy.deepcopy(data)
    score_type_list = {
        'kills': True,
        'zeit': False,
        'platz': False,
        'pvp': False,
        'punkte': True,
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
            for player_tuple in game_round:
                round_number = player_tuple[3]
                player_nickname = player_tuple[1]
        
                if round_number in points_per_game:
                    pointstemp = points_per_game[round_number].get(player_nickname, 0)
                    player_tuple = player_tuple + (pointstemp,)

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
    print("=============================================")
    print("ERGEBNISBERECHNUNG")
    print("=============================================")
    
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