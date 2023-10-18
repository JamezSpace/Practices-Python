user_input = input("Input String: ").lower()
unique_letters = set(user_input)

repeated = lambda str : "Unique" if len(str) == len(unique_letters) else "Deja Vu"
print(repeated(user_input))