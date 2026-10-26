

with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
    print(f"hello {line}")