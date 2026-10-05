def is_funny(string):
    return set(string) <= {"h", "a"}


if __name__ == "__main__":
    print(is_funny("hahahahahaha"))
