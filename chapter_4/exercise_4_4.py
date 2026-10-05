"""Generate dates indefinitely, one second at a time."""


def gen_secs():
    yield from range(60)


def gen_minutes():
    yield from range(60)


def gen_hours():
    yield from range(24)


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f'{hour:02d}:{minute:02d}:{second:02d}'


def gen_years(start=2019):
    # Preserve the starting year in the course's signature and examples.
    while True:
        yield start
        start += 1


def gen_months():
    yield from range(1, 13)


def gen_days(month, leap_year=True):
    lengths = (31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if not 1 <= month <= 12:
        raise ValueError('Month must be between 1 and 12')
    yield from range(1, lengths[month - 1] + 1)


def gen_date():
    for year in gen_years():
        leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield f'{day:02d}/{month:02d}/{year:04d} {time}'


def main():
    dates = gen_date()
    # The first yielded value represents elapsed second zero.
    next(dates)
    while True:
        for _ in range(1_000_000):
            value = next(dates)
        print(value)


if __name__ == '__main__':
    main()
