import itertools
from typing import Union


def test_split_amount() -> bool or None:
    assert split_amount(13, [1, 2, 5]) == [5, 5, 2, 1]
    assert split_amount(13, [1, 10]) == [10, 1, 1, 1]
    assert split_amount(13, [2, 5]) == [5, 2, 2, 2, 2]
    assert split_amount(11.5, [0.5, 1, 10]) == [10, 1, 0.5]
    assert split_amount(11, [5, 2]) == [5, 2, 2, 2]


def find_combinations_with_sum(banknotes_values, target_amount) -> list:
    def backtrack(start, target_amount, current_combination) -> list or None:
        if target_amount == 0:
            result.append(list(current_combination))
            return
        if target_amount < 0 or start == len(banknotes_values):
            return

        for bill in range(start, len(banknotes_values)):
            current_combination.append(banknotes_values[bill])
            backtrack(bill, target_amount - banknotes_values[bill], current_combination)
            current_combination.pop()

    result = []

    backtrack(0, target_amount, [])
    return result


def split_amount(amount: Union[int, float], banknotes: list[Union[int, float]]) -> Union[list, bool]:
    """Returns a list, consisting of biggest banknotes/coins, which can be used to split the amount or False - if it's
    not possible to split the amount into banknotes"""

    banknotes.sort(reverse=True)
    all_possible_combinations = find_combinations_with_sum(banknotes, amount)
    if sum(all_possible_combinations[0]) == amount:
        return all_possible_combinations[0]
    else:
        return False


test_split_amount()
