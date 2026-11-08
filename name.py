name = input("Enter your name: ")

# The key-word "with" allows you to automate the closing of a file
with open("name.txt", "a") as file:
    file.write(f"{name}\n")