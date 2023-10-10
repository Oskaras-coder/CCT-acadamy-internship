import re
from typing import Dict


def find_words_with_repeated_letters(input_filename: str) -> (list, list):

    separators = r'[,.!?:;\n ]+'
    list_of_split_words = re.split(separators, input_filename)
    enumerated_list_of_split_words = enumerate(list_of_split_words)

    duplicated_words = []
    for number, value in enumerated_list_of_split_words:
        is_duplicate = False
        for word_index in range(number + 1, len(list_of_split_words)):
            if list_of_split_words[word_index] == value and value not in duplicated_words:
                letters_list = list(value)
                for letter in letters_list:
                    if letters_list.count(letter) > 1:
                        duplicated_words.append(value)
                        is_duplicate = True
                        break
                if is_duplicate:
                    break
    return duplicated_words, list_of_split_words


def find_counts_of_words_with_repeated_letters(input_filename: str) -> dict[str, int]:
    word_with_repeated_letters, list_of_split_words = find_words_with_repeated_letters(input_filename)
    dictionary_of_repeated_words = {word: list_of_split_words.count(word) for word in word_with_repeated_letters}
    return dictionary_of_repeated_words


def find_repeated_letters_counts_in_words(input_filename: str) -> dict[str, int]:
    repeated_words = find_counts_of_words_with_repeated_letters(input_filename)
    for word in repeated_words:
        repeated_words[word] = {letter: word.count(letter) for letter in word if word.count(letter) > 1}
    return repeated_words


with open("input_words.txt") as filename:
    text = filename.read().lower()

duplicated_words, split_words = find_words_with_repeated_letters(text)
print(duplicated_words)
print(find_counts_of_words_with_repeated_letters(text))
print(find_repeated_letters_counts_in_words(text))
