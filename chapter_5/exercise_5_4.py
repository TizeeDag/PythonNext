"""Validate and generate nine-digit ID numbers for the course exercise."""
MAX_ID = 999999999


def check_id_valid(id_number):
    """Return whether an integer in the nine-digit range passes the checksum."""
    if type(id_number) is not int or not 0 <= id_number <= MAX_ID:
        return False
    products = [int(digit) * (1 + index % 2) for index, digit in enumerate(f'{id_number:09d}')]
    return sum(product if product < 10 else product // 10 + product % 10 for product in products) % 10 == 0


class IDIterator:
    """Produce valid IDs strictly after the supplied initial ID."""
    def __init__(self, id_):
        if type(id_) is not int or not 0 <= id_ <= MAX_ID:
            raise ValueError('ID must be an integer from 0 to 999999999')
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        while self.id_ < MAX_ID:
            self.id_ += 1
            if check_id_valid(self.id_):
                return self.id_
        raise StopIteration


def id_generator(id_number):
    """Yield valid IDs after id_number, stopping at 999999999."""
    if type(id_number) is not int or not 0 <= id_number <= MAX_ID:
        raise ValueError('ID must be an integer from 0 to 999999999')
    for candidate in range(id_number + 1, MAX_ID + 1):
        if check_id_valid(candidate):
            yield candidate


def main():
    id_number = int(input('Enter ID: '))
    choice = input('Generator or Iterator? (gen/it)? ')
    source = IDIterator(id_number) if choice == 'it' else id_generator(id_number)
    for _ in range(10):
        print(next(source))


if __name__ == '__main__':
    main()
