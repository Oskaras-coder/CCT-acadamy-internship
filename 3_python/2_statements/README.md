# 1. Task: conditional statements

Implement a function `get_number_stats(numbers: list) -> dict`, which returns dictionary with these values:
  - `max` - maximum number from the list. 
  - `min` - minimum numbers from the list.
  - `average` - average number (sum/len) from the list.
  - `in_interval_count` - how many numbers are in interval [0, 10].
  - `positive_count` - how many positive numbers.
  - `negative_count` - how many negative numbers.
  - `zero_count` - how many numbers are equal to 0.
  - `positive_sum` - total sum of positive numbers.
  - `negative_sum` - total sum of negative numbers.

## Material
- https://docs.python.org/3/tutorial/controlflow.html#if-statements
- https://docs.python.org/3/library/functions.html#sum
- https://docs.python.org/3/library/functions.html#len


# 2. Task: indexes in a for loop
Implement a function `get_max_pair_sum(numbers: list) -> float`, which returns maximum value of 
`a1 + a2, a2 + a3, ..., an-1 + an`, where `a1, ..., aN` are numbers in the list.

## Material
- https://docs.python.org/3/library/functions.html#enumerate


# 3.1. Task: data structure in a dictionary
Implement a function `find_words_with_repeated_letters(input_filename: str) -> list[str]`, which returns
a list of words, which have repeated more than once in the text and have duplicate letters
(e.g. word "letters" have duplicate "e" and "t"). Feel free to use text provided in `intput_wrods.txt` file.

Bonus points for providing:
- the frequency of those words by implementing:
`find_counts_of_words_with_repeated_letters(input_filename: str) -> dict[str, int]`.
- which letters were repeated in each word and how many times:
`find_repeated_letters_counts_in_words(input_filename: str) -> dict[str, dict[str, int]]`.

Note: separators such as `,.!?:;` are not letters.

## Material
- https://docs.python.org/3/library/stdtypes.html#str.split
- https://docs.python.org/3/library/stdtypes.html#str.strip


# 3.2. Optional:
Find sentences, which have at least two different words with repeated letters.
The output should contain this information:
- full sentence (including separators), which meets the condition stated previously.
- how many times has this sentence appeared in the text.
- which words in the sentence has repeated letters, and:
    - how many times were these words repeated in the sentence.
    - how many times were these words repeated in the whole text.

# 3.3. Optional:
Update 3.2. code to ignore text parts which are in the `()` brackets.
