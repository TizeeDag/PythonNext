"""Generate the unbounded Fibonacci sequence."""
def get_fibo():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


if __name__ == '__main__':
    from itertools import islice
    for value in islice(get_fibo(), 4):
        print(value)
