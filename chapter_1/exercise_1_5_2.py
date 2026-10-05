with open("names.txt", encoding="utf-8") as names:
    print(sum(map(len, names.read().splitlines())))
