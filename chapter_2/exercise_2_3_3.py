class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    first = Octopus("Inky")
    second = Octopus()
    print(first.get_name())
    print(second.get_name())
    first.set_name("Ollie")
    print(first.get_name())
    print(Octopus.count_animals)


if __name__ == "__main__":
    main()
