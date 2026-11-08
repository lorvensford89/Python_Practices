
# The key-word "with" allows you to automate the closing of a file
with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"hello {line.rstrip()}")