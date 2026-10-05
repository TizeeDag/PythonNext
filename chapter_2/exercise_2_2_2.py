class Octopus:
    def __init__(self):
        self._name = "Octavio"
        self._age = 0

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


def main():
    first = Octopus()
    second = Octopus()
    first.birthday()
    print(first.get_age())
    print(second.get_age())


if __name__ == "__main__":
    main()
