def main():
    # TODO:
    problem_set3()



def problem_set3():
    # TODO
    """
    In a file called grocery.py, implement a program that prompts the user 
    for items, one per line, until the user inputs control-d (which is a 
    common way of ending one’s input to a program). Then output the user’s 
    grocery list in all uppercase, sorted alphabetically by item, prefixing 
    each line with the number of times the user inputted that item. No need
    to pluralize the items. Treat the user’s input case-insensitively.
    """

    items = []

    while True:
        try:
            user_input = input("").upper()
            items.append(user_input)
        except EOFError:
            pass
            print("")
            items.sort()
            for i in sorted(set(items)): # iterate through a sorted unique-item list
                count_items = items.count(i)
                print(count_items, i)
            break
    
           
if __name__ == "__main__":
    main()


