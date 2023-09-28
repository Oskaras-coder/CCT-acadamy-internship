import itertools
from typing import Union


def test_split_amount() -> bool or None:
    assert split_amount(1, {10: 100}) == False
    assert split_amount(100, {10: 100, 20: 1, 50: 1}) == [50, 20, 10, 10, 10]
    assert split_amount(13, {1: 10, 2: 1, 5: 5}) == [5, 5, 2, 1]
    assert split_amount(13, {1: 10, 2: 1, 5: 1}) == [5, 2, 1, 1, 1, 1, 1, 1]
    assert split_amount(11, {2: 4, 5: 2}) == [5, 2, 2, 2]
    assert split_amount(117, {2: 3, 5: 4, 10: 1, 100: 20}) == [100, 10, 5, 2]
    assert split_amount(167, {1: 10, 2: 4, 5: 7, 50: 2, 100: 2}) == [100, 50, 5, 5, 5, 2]
    assert not split_amount(13, {2: 30, 10: 70})
    assert not split_amount(13.5, {2: 20, 10: 5})
    assert split_amount(130.5, {0.5: 4, 10: 15, 20: 14, 50: 2}) == [50, 50, 20, 10, 0.5]
    assert split_amount(1.5, {0.1: 3, 0.2: 10}) == [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1]
    assert split_amount(1.5, {0.1: 3, 0.2: 10, 0.5: 1}) == [0.5, 0.2, 0.2, 0.2, 0.2, 0.2]
    assert split_amount(0.77, {0.01: 10, 0.05: 3, 0.1: 2, 0.2: 6})
    assert split_amount(0.77, {0.01: 10, 0.05: 3, 0.1: 2, 0.2: 6}) == [0.2, 0.2, 0.2, 0.1, 0.05, 0.01, 0.01]
    assert split_amount(100, {10: 100, 20: 1, 50: 1}) == [50, 20, 10, 10, 10]


def find_combinations_with_sum(banknotes_values, target_amount) -> list:
    """Recursive algorithm"""

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


def iterative_algorithm(amount, banknotes_values, banknotes_amount):
    """Iterative algorithm"""
    is_found = False
    for bill in range(0, int(amount / banknotes_values[-1])):
        for seq in itertools.combinations_with_replacement(banknotes_values, bill):
            if round(sum(seq), 2) == amount:
                is_found = False
                for value in banknotes_values:
                    if banknotes_amount.count(round(value,2)) >= seq.count(round(value,2)):
                        is_found = True
                    else:
                        is_found = False
                        break
                if is_found:
                    return list(seq)
    return is_found


def split_amount(amount: Union[int, float], banknotes: dict) -> Union[list, bool]:
    """Returns a list, consisting of the biggest banknotes/coins, which can be used to split the amount or False - if it's
    not possible to split the amount into banknotes"""

    list_of_available_banknotes = [item for bill, bill_amount in banknotes.items() for item in [bill] * bill_amount]
    list_of_available_banknotes.sort(reverse=True)
    list_of_banknotes = list(banknotes.keys())
    list_of_banknotes.sort(reverse=True)
    # all_possible_combinations = find_combinations_with_sum(list_of_available_banknotes, amount)
    iterative_answer = iterative_algorithm(amount, list_of_banknotes, list_of_available_banknotes)
    return iterative_answer


test_split_amount()
