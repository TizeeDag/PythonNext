with open("names.txt", encoding="utf-8") as names:
    print(max(names.read().splitlines(), key=len))
