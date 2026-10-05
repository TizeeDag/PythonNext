def is_prime(number):
    return number > 1 and not [divisor for divisor in range(2, int(number ** 0.5) + 1) if number % divisor == 0]


if __name__ == "__main__":
    print(is_prime(42))
    print(is_prime(43))
