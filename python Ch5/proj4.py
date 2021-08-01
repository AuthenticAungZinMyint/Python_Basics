#geek translator
#Demo using dictionaries
geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque" : "the collection of debris found in computer keyboards.",
        "Link Rot" : "the process by which web page links become obsolete.",
        "Percussive Maintenance" : "the act of striking an electronic device to make it work.",
        "Uninstalled" : "being fired.  Especially popular during the dot-bomb era."}
choice = None
while choice != 0:
    print(
    """
    Geek Translator
    0 - Quit
    1 - Look Up a Geek Term
    2 - Add a geek term
    3 - Redefine a Geek term
    4 - Delete a Geek term
    """
    )
    choice = input("Choice:")

#Exit
    if choice == "0":
        print("Goodbye.")
#get a definition
    elif choice == "1":
        term = input("What term do you want me to translate?:")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)
#add the term definition pair
    elif choice == "2":
        term = input("What term do you want me to add?:")
        if term not in geek:
            definition = input("\nWhat's the deninition?:")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exist! Try redefining it>")
            geek[term] = definition
#redefining an existing term
    elif choice == "3":
        term = input("What term do you want me to redefine?")
        if term in geek:
            definition = input("What's the new definition:")
            geek[term] = definition
            print("\n", term, "has been redefined.")
        else:
            print("\nTerm doesn't exist! Try adding it.")
            geek[term] = definition
#delete a term definitin pair
    elif choice == "4":
        term = input("what term doo you ant to delete?:")
        if term in geek:
            del geek[term]
            print("\nOkay, Deleted", term)
        else:
                print("\nI can't do that!", term, "doesn't exist in the dictionary.")
#some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
        input("\n\nPress the enter key to exit")
    

    


