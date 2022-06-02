# Task: Basketball game statistics

Statistics is being recorded during every game. This statistics is used for further games. 
The total number of players `n` (`n < 13`), who have participated in the games,
is provided in the first line of data file `input_data.txt`. 
Six natural numbers are provided in each following row:
- first number - the number of a player, 
- next two numbers - how long did the player play (minutes and seconds),
- following numbers - how many two-points, three-points and free throws did that player score.

Implement the program, which would provide these statistic measurements:
- number of a player, which scored the most points. If there are several such players - provide the one with lowest player number.
- number of a player, who played the least amount of time. If there are several such players - provide the one with the highest player number.
- number of a player, who scored the most three-points. If there are several such players - provide the one with lowest player number.
- how many points scored by throwing two-points.
- how many points scored by free throws.
- how many points in total scored during the game.

The output should be written into `output_data.txt` file.
Implement function for reading/writing data from/to a file.
Also a function should be used to calculate each statistic.
Implement unit tests for functions which calculate statistics.
