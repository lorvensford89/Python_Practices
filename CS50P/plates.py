def main():
    plate = input("Plate: ")
    if is_valid(plate) and mid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return s[:2].isalpha() and 2 <= len(s) <= 6



def mid(m):
    first_digit_index = -1

    # Find the index of the first digit
    for i, j in enumerate(m):
        if j.isdigit():
            first_digit_index = i
            break

    # If there are no digits at all, it's fine (all letters)
    if first_digit_index == -1:
        return True

    # If the first number is 0, not allowed
    if m[first_digit_index] == "0":
        return False

    # After the first number, everything must be digits
    if not m[first_digit_index:].isdigit():
        return False

    return True




main()