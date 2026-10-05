length = int(input("Enter name length: "))
with open("names.txt", encoding="utf-8") as names:
    print("\n".join([name for name in names.read().splitlines() if len(name) == length]))
