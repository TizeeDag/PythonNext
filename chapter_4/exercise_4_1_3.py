"""Lazily find the first prime strictly greater than n."""
from itertools import count
from math import isqrt


def is_prime(n):
    return n > 1 and all(n % divisor for divisor in range(2, isqrt(n) + 1))


def first_prime_over(n):
    primes = (candidate for candidate in count(max(2, n + 1)) if is_prime(candidate))
    return next(primes)


if __name__ == '__main__':
    print(first_prime_over(1000000))
