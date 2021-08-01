#High score 2.0
#Demo nested sequences
scores =[]
choice = None
while choice != "0":
    print(
        """
        High Scores 2.0
        0 - Quit
        1 - List Scores
        2 - Add a score
        """
        )
    choice = input("choice:")
    print()
    if choice == "0":
        print("Goodbye")
#display high scores table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
#add a score
    elif choice == "2":
        name = input("what's the player's name?:")
        score = int(input("What's score did the player get?:"))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #keep only top 5 scores
#soe unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
    input ("\n\nPress the enter key to exit")
