from typing import Union

def test_split_amount() -> bool or None:
    assert split_amount(11, [5, 2, 1]) == [5, 5, 1]
    assert split_amount(13, [1, 2, 5]) == [5, 5, 2, 1]
    assert split_amount(13, [1, 10]) == [10, 1, 1, 1]
    assert split_amount(13, [2, 5]) == False
    assert split_amount(11.5, [0.5, 1, 10]) == [10, 1, 0.5]
    print(split_amount(11, [5, 2]))
    # assert split_amount(11, [5, 2]) == [5, 2, 2, 2]


def split_amount(amount: Union[int, float], banknotes: list) -> Union[list, bool]:
    """Returns a list, consisting of biggest banknotes/coins, which can be used to split the amount or False - if it's
    not possible to split the amount into banknotes"""
    banknotes.sort(reverse=True)
    split_banknotes = []
    for money_values in banknotes:
        while amount // money_values != 0:
            split_banknotes.append(money_values)
            amount -= money_values
    if amount != 0:
        split_banknotes = False
    return split_banknotes


test_split_amount()
