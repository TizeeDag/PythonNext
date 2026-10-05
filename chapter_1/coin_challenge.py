def combine_coins(coin, numbers):
    return ", ".join(map(lambda number: coin + str(number), numbers))


if __name__ == "__main__":
    print(combine_coins("$", range(5)))
