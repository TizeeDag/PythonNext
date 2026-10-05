"""Print every third number without an if statement."""
from itertools import islice


def main():
    numbers = iter(list(range(1, 101)))
    for number in islice(numbers, 2, None, 3):
        print(number)


if __name__ == '__main__':
    main()
