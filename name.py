names = []

# The key-word "with" allows you to automate the closing of a file
with open("name.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello {name}")