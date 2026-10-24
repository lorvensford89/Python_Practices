def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            print(gauge(percentage))
            break


def convert(fraction):
    parts = fraction.split("/")

    if len(parts) != 2:
        raise ValueError

    x = int(parts[0])
    y = int(parts[1])

    if x < 0 or y < 0 or x > y:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()