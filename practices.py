import inflect

def main():

    p = inflect.engine()

    count = 233
    print(f"There {p.plural_verb("was", count), {p.number_to_words(count)}, {p.plural_noun("person", count)}} by the door.")

    

if __name__ == "__main__":
    main()