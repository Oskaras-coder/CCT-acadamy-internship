import itertools
from typing import Union, List


def test_split_amount() -> Union[bool, None]:
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
    assert split_amount(0.77, {0.01: 10, 0.05: 3, 0.1: 2, 0.2: 6}) == [0.2, 0.2, 0.2, 0.1, 0.05, 0.01, 0.01]
    assert split_amount(100, {10: 100, 20: 1, 50: 1}) == [50, 20, 10, 10, 10]
    assert split_amount(1, {10: 100}) == False


def recursive_algorithm(amount: Union[int, float], banknotes_values: List[Union[int, float]],
                        banknotes_amount: List[int]):
    def calculating_best_combination(start: Union[int, float], amount: Union[int, float],
                                     current_combination: List[Union[int, float]]) -> Union[list, None]:
        if round(amount, 2) == 0:
            is_found = False
            for value in banknotes_values:
                if banknotes_amount.count(round(value, 2)) >= current_combination.count(round(value, 2)):
                    is_found = True
                else:
                    is_found = False
                    break
            if is_found:
                return current_combination
            return
        if amount < 0 or start == len(banknotes_values):
            return

        for bill in range(start, len(banknotes_values)):
            current_combination.append(banknotes_values[round(bill, 2)])
            result = calculating_best_combination(bill, amount - banknotes_values[round(bill, 2)], current_combination)
            if result:
                return result
            current_combination.pop()

    return calculating_best_combination(0, amount, [])


def iterative_algorithm(amount: Union[int, float], banknotes_values: list, banknotes_amount: List[Union[int, float]]) \
        -> Union[list, bool]:
    """Iterative algorithm"""
    is_found = False
    for bill in range(0, int(amount / banknotes_values[-1])):
        for combination in itertools.combinations_with_replacement(banknotes_values, bill):
            if round(sum(combination), 2) == amount:
                is_found = False
                for value in banknotes_values:
                    if banknotes_amount.count(round(value, 2)) >= combination.count(round(value, 2)):
                        is_found = True
                    else:
                        is_found = False
                        break
                if is_found:
                    return list(combination)
    return is_found


def split_amount(amount: Union[int, float], banknotes: dict) -> Union[list, bool]:
    """Returns a list, consisting of the biggest banknotes/coins, which can be used to split the amount or False - if it's
    not possible to split the amount into banknotes"""

    list_of_available_banknotes = [item for bill, bill_amount in banknotes.items() for item in [bill] * bill_amount]
    list_of_available_banknotes.sort(reverse=True)
    list_of_banknotes = list(banknotes.keys())
    list_of_banknotes.sort(reverse=True)

    iterative_answer = iterative_algorithm(amount, list_of_banknotes, list_of_available_banknotes)
    recursive_answer = recursive_algorithm(amount, list_of_banknotes, list_of_available_banknotes)
    if iterative_answer == recursive_answer:
        return recursive_answer
    elif recursive_answer is None:
        return False


test_split_amount()
