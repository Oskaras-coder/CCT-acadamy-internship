# Task1: Using lists
1. Write an expression which calculates the average of a list
2. Write an expression, which calculates average of even
list elements (with indexes 0, 2, 4, ..).
3. Write an expression, which finds the average value of the
provided list, ignoring the 25% smallest and 25% highest list values.
4. Test your expressions with the `ranks` list provided below to check your results: 
```
ranks = [22, 83, 60, 15, 29, 89, 93, 86, 33, 39, 77, 61, 83, 77, 65, 42, 14, 33, 20, 86,
         4, 13, 29, 40, 85, 92, 56, 94, 82, 98, 20, 41, 50, 4, 3, 48, 15, 29, 40, 90]
```
Returned values should be equal to: `51.0` (step 1.), 44.0 (step 2.) and 50.7 (step 3.).


# Task2: Using dictionaries
1. write an expression, which constructs a new dictionary (from already defined one)
with keys `name` and `karma` (if a key is not present in provided dict - use `"Unknown"` instead).
2. test your expression with these dictionaries (print the result):
```
p1 = {'name': 'Foo', 'karma': 123, 'value': -1}
p2 = {'karma': 123, 'value': -1}
p3 = {'name': 'Foo', 'value': -1}
```

# Task3: Basketball game statistics
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
