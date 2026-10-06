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
            count_items = items.count(user_input) # To fix
            items = list(set(items))
            items.sort()
        except EOFError:
            pass
            print("")
            for i in range(len(items)):
                print(count_items, items[i])
            break
    
           
            


            



if __name__ == "__main__":
    main()


