def main():
    plate2 = input("Plate: ")
    if is_valid(plate2):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if not (s[:2].isalpha() and 2 <= len(s) <= 6):
        return False

    first_digit_index = -1

    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break

    # No digits means the string contains only letters, so it's valid
    if first_digit_index == -1:
        return True

    # The first digit cannot be 0, and all following characters must be digits
    if s[first_digit_index] == "0":
        return False

    return s[first_digit_index:].isdigit()


if __name__ == "__main__":
    main()