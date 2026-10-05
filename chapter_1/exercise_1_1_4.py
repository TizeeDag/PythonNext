def sum_of_digits(number):
    return sum(map(int, str(abs(number))))


if __name__ == "__main__":
    print(sum_of_digits(104))
