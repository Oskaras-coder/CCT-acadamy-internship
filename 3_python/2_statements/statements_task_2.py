def get_max_pair_sum(numbers: list) -> float:  # Trying to use both enumerate and except methods, possible simpler
    # solution
    enumerated_numbers_list = enumerate(numbers)
    highest_number = None
    for index, number in enumerated_numbers_list:
        try:
            highest_pair = numbers[index] + numbers[index + 1]
        except IndexError:
            break
        else:
            if highest_number is None or highest_number < highest_pair:
                highest_number = highest_pair

    return highest_number


max_pair = get_max_pair_sum([12, 12, 10, 0, 1, 15])
assert max_pair == 24
