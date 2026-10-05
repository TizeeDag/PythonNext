with open("names.txt", encoding="utf-8") as names_file:
    names = names_file.read().splitlines()
shortest_length = min(map(len, names))
print("\n".join([name for name in names if len(name) == shortest_length]))
