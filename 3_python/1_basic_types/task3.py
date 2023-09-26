with open("input_data.txt") as list_data:
    list_values = list_data.read().splitlines()
    player_number = list_values[0]

    players_data = [data.split(" ") for data in list_values[1:]]
    print(player_number)
    print(players_data)

    def score_calculator(two, three, free):
        score = two * 2 + three * 3 + free
        return score

    def most_scored_player(data):
        highest_score = 0
        most_scored_players_number = None
        for p in data:
            player_score = score_calculator(data[p]['two_pointers'], data[p]['three_pointers'], data[p]["free_throws"])
            if player_score >= highest_score or most_scored_players_number is None and most_scored_players_number > p:
                most_scored_players_number = p
                highest_score = player_score
        return most_scored_players_number

    def least_amount_played(data):
        least_time = None
        least_played_players_number = None
        for p in data:
            time_played = data[p]['played_time_secs']
            if least_time is None or least_played_players_number is None or least_time > time_played and least_played_players_number < p:
                least_played_players_number = p
                least_time = time_played
        return least_played_players_number


    def most_three_pointers(data):
        most_three = 0
        most_three_pointers_players_number = float("inf")
        for p in data:
            three_scored = data[p]['three_pointers']
            if most_three < three_scored and most_three_pointers_players_number > p:
                most_three = three_scored
                most_three_pointers_players_number = p

        return most_three_pointers_players_number


    def two_points_count(data):
        total = 0
        for p in data:
            total += data[p]['two_pointers'] * 2
        return total

    def free_throws_count(data):
        total = 0
        for p in data:
            total += data[p]['free_throws']
        return total

    def total_count(data):
        total_score = 0

        for p in data:
            total_score += score_calculator(data[p]['two_pointers'], data[p]['three_pointers'], data[p]["free_throws"])
        return total_score


    players_attributes = {}

    for player in players_data:
        player = [int(i) for i in player]
        players_attributes[player[0]] = {}
        for attribute in players_data:
            players_attributes[player[0]]["played_time_secs"] = player[1] * 60 + player[2]
            players_attributes[player[0]]["two_pointers"] = player[3]
            players_attributes[player[0]]["three_pointers"] = player[4]
            players_attributes[player[0]]["free_throws"] = player[5]

print(players_attributes)
print(most_scored_player(players_attributes))
print(least_amount_played(players_attributes))
print(most_three_pointers(players_attributes))
print(two_points_count(players_attributes))
print(free_throws_count(players_attributes))
print(total_count(players_attributes))

with open("output_data.txt", mode="w") as file:
    file.write(f"Number of a player, which scored the most points - {most_scored_player(players_attributes)}\n"
               f"Number of a player, who played the least amount of time - {least_amount_played(players_attributes)}\n"
               f"Number of a player, who scored the most three-points - {most_three_pointers(players_attributes)}\n"
               f"Points scored by throwing two-points - {two_points_count(players_attributes)}\n"
               f"Points scored by free throws - {free_throws_count(players_attributes)}\n"
               f"Points in total scored during the game - {total_count(players_attributes)}\n")