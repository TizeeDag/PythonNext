"""Flatten inclusive ranges through a pipeline of generator expressions."""
def parse_ranges(ranges_string):
    bounds = (tuple(map(int, part.split('-'))) for part in ranges_string.split(','))
    return (number for start, end in bounds for number in range(start, end + 1))


if __name__ == '__main__':
    print(list(parse_ranges('1-2,4-4,8-10')))
    print(list(parse_ranges('0-0,4-8,20-21,43-45')))
