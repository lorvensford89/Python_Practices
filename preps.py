def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]


    print(len(months))
    print("")

    user_input = input("Date: ")
    three_parts = user_input.split(",")

    print(three_parts)
    print(three_parts[0])
    print(int(three_parts[1]))
    print("")
    second_split = three_parts[0].split(" ")
    print(second_split)
    print(second_split[0])
    print(second_split[1])

if __name__ == "__main__":
    main()
