def intersection(list_1, list_2):
    return [value for index, value in enumerate(list_1) if value in list_2 and value not in list_1[:index]]


if __name__ == "__main__":
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
