"""Task 1"""


def find_average(list):
    average_of_the_list = float(round(sum(list) / len(list), 1))
    return average_of_the_list


def find_average_even_index(list2):
    ranks2 = list2[::2]
    average_of_even_list_elements = float(round(sum(ranks2) / len(ranks2), 1))
    return average_of_even_list_elements


def find_average_25_75_percentile(list3):
    list3.sort()
    ranks3 = ranks[int(len(list3) * 0.25):int(len(list3) * 0.75)]
    average_25_75_of_the_list = float(round(sum(ranks3) / len(ranks3), 1))
    return average_25_75_of_the_list


ranks = [22, 83, 60, 15, 29, 89, 93, 86, 33, 39, 77, 61, 83, 77, 65, 42, 14, 33, 20, 86,
         4, 13, 29, 40, 85, 92, 56, 94, 82, 98, 20, 41, 50, 4, 3, 48, 15, 29, 40, 90]

assert find_average(ranks) == 51.0
assert find_average_even_index(ranks) == 44.0
assert find_average_25_75_percentile(ranks) == 50.7