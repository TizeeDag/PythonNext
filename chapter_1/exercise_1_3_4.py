password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print("".join([chr((ord(char) - ord("a") + 2) % 26 + ord("a")) if "a" <= char <= "z" else char for char in password]))
