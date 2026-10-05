"""Find distinct ways to make $100 with the available bills."""
from itertools import product


def possibilities():
    for counts in product(range(4), range(6), range(3), range(6)):
        if sum(count * value for count, value in zip(counts, (20, 10, 5, 1))) == 100:
            yield tuple(value for count, value in zip(counts, (20, 10, 5, 1)) for _ in range(count))


if __name__ == '__main__':
    options = list(possibilities())
    for option in options:
        print(option)
    print('Number of possibilities:', len(options))
