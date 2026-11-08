
# The key-word "with" allows you to automate the closing of a file
with open("name.txt", "r") as file:
    for line in file:
        print(f"hello {line.rstrip()}")