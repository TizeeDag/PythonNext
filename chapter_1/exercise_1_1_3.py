def four_dividers(number):
    return list(filter(lambda value: value % 4 == 0, range(1, number + 1)))


if __name__ == "__main__":
    print(four_dividers(9))
    print(four_dividers(3))
