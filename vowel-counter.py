vowels = ('a', 'e', 'i', 'o', 'u')
user_input = input("Input String: ")
count_vowels = len([char for char in user_input if char.lower() in vowels])

print(f"Number of Vowels: {count_vowels}")