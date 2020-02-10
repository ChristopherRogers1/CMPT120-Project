def getPaid(wallet):
    return 10 + wallet

def main():

    print()
    print("---------------------------")
    print("Welcome to THE HEROIC TALE!")
    print("---------------------------")
    print()

    print("Let's start with some information about yourself, traveler. What is your name?")

    name = input("")
    
    print("Welcome to Eawrsa, " + name + ". Remind me, where do you come from?")

    home = input("")

    print("Interesting. Only one more question, what was your profession in your homeland?")

    job = input("")

    print("Ah yes, " + name + ", the great " + job + " of " + home + ".")

    wallet = 0

    print("It's getting late, and you've got a long day ahead of you; why not take a nap?")

    input("Press enter to go to sleep...")

    print("...")

    print("You awake to a fire! Your home is burning down! In a panic, you run to the exit, leaving behind all of your money and belongings. The town is being pillaged by the badguyians to the north! You run to the east, towards the woods. Once you arrive, you find a crisp ten dollar coin. Sweet!")

    wallet = getPaid(wallet)

    print("You now have " + str(wallet) + " dollars.")

    input("Press enter to travel into the forest...")

    print("You travel deeper into the forest, leaving your burning town behind.
main()


