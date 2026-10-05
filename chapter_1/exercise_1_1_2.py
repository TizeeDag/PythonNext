def double_letter(my_str):
    return "".join(map(lambda letter: letter * 2, my_str))


if __name__ == "__main__":
    print(double_letter("python"))
    print(double_letter("we are the champions!"))
