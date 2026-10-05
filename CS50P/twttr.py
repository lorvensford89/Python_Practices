user_input = input("Input: ")
output = ("")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for vowel in user_input:
    if not vowel in vowels:
        output += vowel

print("Output:", output)