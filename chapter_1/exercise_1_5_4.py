with open("names.txt", encoding="utf-8") as source, open("name_length.txt", "w", encoding="utf-8") as target:
    target.write("\n".join(map(str, map(len, source.read().splitlines()))) + "\n")
