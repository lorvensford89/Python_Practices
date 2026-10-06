def main():
    # TODO:
    problem_set3()



def problem_set3():
    # TODO:
    """
    In a file called outdated.py, implement a program that prompts the
    user for a date, anno Domini, in month-day-year order, formatted like
    9/8/1636 or September 8, 1636, wherein the month in the latter might
    be any of the values in the list below:
    """

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

    """
    Then output that same date in YYYY-MM-DD format. If the user’s
    input is not a valid date in either format, prompt the user again.
    Assume that every month has no more than 31 days; no need to validate
    whether a month has 28, 29, 30, or 31 days.
    """

    # months <= 31
    # Two formats are required from month-day-year order: 9/8/1636 AND September 8, 1636

    while True:
        try:
            user_input = input("Date: ")

            if "/" in user_input:
                three_parts = user_input.split("/")
                # 9/8/1636 format
                m = int(three_parts[0])
                d = int(three_parts[1])
                y = int(three_parts[2])
            elif "," in user_input:
                # September 8, 1636 format
                first_split = user_input.split(",")      # September, 8 | 1636
                second_split = first_split[0].split(" ") # September | 8
                m2 = second_split[0]
                if m2 not in months:
                    continue
                m = int(months.index(m2)) + 1
                d = int(second_split[1])
                y = int(first_split[1])
            else:
                continue

        except (ValueError, IndexError):
            pass
            continue
        else:
            # Number of days and months limit
            if d > 31 or m > len(months):
                continue
            # print the normal date format
            print(f"{y:04}-{m:02}-{d:02}", end="")
            break



if __name__ == "__main__":
    main()
