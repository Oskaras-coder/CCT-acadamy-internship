def get_number_stats(numbers: list) -> dict:
    in_interval_count, positive_count, negative_count, zero_count = 0, 0, 0, 0
    for number in numbers:
        if 0 <= number <= 10:
            in_interval_count += 1
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    task_1_dictionary = {"max": max(numbers),
                         "min": min(numbers),
                         "average": sum(numbers) / len(numbers),
                         "in_interval_count": in_interval_count,
                         "positive_count": positive_count,
                         "negative_count": negative_count,
                         "zero_count": zero_count,
                         "positive_sum": sum([number for number in numbers if number > 0]),
                         "negative_sum": sum([number for number in numbers if number < 0]),
                         }
    return task_1_dictionary

print(get_number_stats([5, 7, 10, 2, -10, 0, 0, 0]))