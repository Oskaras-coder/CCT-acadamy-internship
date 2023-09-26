def score_calculator(two_score, three_score, free_score):
    score = two_score * 2 + three_score * 3 + free_score
    return score


def most_scored_player(data):
    highest_score = 0
    most_scored_players_number = None
    for player_data_in_dic in data:
        player_score = score_calculator(data[player_data_in_dic]['two_pointers'], data[player_data_in_dic]['three_pointers'], data[player_data_in_dic]["free_throws"])
        if player_score > highest_score or most_scored_players_number is None and most_scored_players_number > player_data_in_dic:
            most_scored_players_number = player_data_in_dic
            highest_score = player_score
    return most_scored_players_number


def least_amount_played(data):
    least_time = None
    least_played_players_number = None
    for player_data_in_dic in data:
        time_played = data[player_data_in_dic]['played_time_secs']
        if least_time is None or least_played_players_number is None or least_time > time_played and least_played_players_number < player_data_in_dic:
            least_played_players_number = player_data_in_dic
            least_time = time_played
    return least_played_players_number


def most_three_pointers(data):
    most_three = 0
    most_three_pointers_players_number = float("inf")
    for player_data_in_dic in data:
        three_scored = data[player_data_in_dic]['three_pointers']
        if most_three < three_scored and most_three_pointers_players_number > player_data_in_dic:
            most_three = three_scored
            most_three_pointers_players_number = player_data_in_dic
    return most_three_pointers_players_number


def two_points_count(data):
    total = sum(data[player_data_in_dic]['two_pointers'] * 2 for player_data_in_dic in data)
    return total


def free_throws_count(data):
    total = sum(data[player_data_in_dic]['free_throws'] for player_data_in_dic in data)
    return total


def total_count(data):
    total_score = sum(score_calculator(data[player_data_in_dic]['two_pointers'], data[player_data_in_dic]['three_pointers'], data[player_data_in_dic]["free_throws"]) for player_data_in_dic in data)
    return total_score


with open("input_data.txt") as list_data:
    list_values = list_data.read().splitlines()
    player_number = int(list_values[0])

if player_number < 13:
    players_data = [data.split(" ") for data in list_values[1:]]
    players_attributes = {}

    for player in players_data:
        player = [int(i) for i in player]
        players_attributes[player[0]] = {}
        for attribute in players_data:
            players_attributes[player[0]]["played_time_secs"] = player[1] * 60 + player[2]
            players_attributes[player[0]]["two_pointers"] = player[3]
            players_attributes[player[0]]["three_pointers"] = player[4]
            players_attributes[player[0]]["free_throws"] = player[5]

    assert (most_scored_player(players_attributes)) == 17
    assert (least_amount_played(players_attributes)) == 23
    assert (most_three_pointers(players_attributes)) == 13
    assert (two_points_count(players_attributes)) == 58
    assert (free_throws_count(players_attributes)) == 22
    assert (total_count(players_attributes)) == 95

    with open("output_data.txt", mode="w") as file:
        file.write(f"Number of a player, which scored the most points - {most_scored_player(players_attributes)}\n"
                   f"Number of a player, who played the least amount of time - {least_amount_played(players_attributes)}\n"
                   f"Number of a player, who scored the most three-points - {most_three_pointers(players_attributes)}\n"
                   f"Points scored by throwing two-points - {two_points_count(players_attributes)}\n"
                   f"Points scored by free throws - {free_throws_count(players_attributes)}\n"
                   f"Points in total scored during the game - {total_count(players_attributes)}\n")
else:
    with open("output_data.txt", mode="w") as file:
        file.write("Players number is too high.")
