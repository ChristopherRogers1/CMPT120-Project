def getPaid(wallet):
    return 10 + wallet

def main():

    text1 = "Let's start with some information about yourself, traveler. What is your name?"
    text3 = "Interesting. Only one more question, what was your profession in your homeland?"
    text4 = "It's getting late, and you've got a long day ahead of you; why not take a nap?"
    text5 = "You awake to a fire! Your home is burning down! In a panic, you run to the exit, leaving behind all of your money and belongings. The town is being pillaged by the badguyians to the north! You run to the east, towards the woods. Once you arrive, you find a crisp ten dollar coin. Sweet!"
    text7 = "You eventually make your way out of the deep forest to be met by a crude gravel road. You travel down the road away from your destroyed home, and eventually come across a lone figure. He is wearing the armor of the northerners which attacked your home. In a fit of rage, you rush him and throw a punch, which somehow luckily connects with a vital organ, killing him instantly. You loot his body, taking what money he had on him."
    text8 = "After a long day of traveling, you lay down your head and rest. Who knows what lay ahead of you?"
    
    print()
    print("---------------------------")
    print("Welcome to THE HEROIC TALE!")
    print("---------------------------")
    print()

    print(text1)

    name = input("")

    text2 = "Welcome to Eawrsa, " + name + ". Remind me, where do you come from?"
    text6 = "You travel deeper into the forest, leaving your burning town behind. As you travel, you wander across one of your neighbors. 'Thank godness it is " + name + "!', they exclaim. They offer you 10 coins in exchange for helping them gather food. You agree, and become 10 coins richer."
    
    print(text2)

    home = input("")

    print(text3)

    job = input("")

    print("Ah yes, " + name + ", the great " + job + " of " + home + ".")

    wallet = 0

    print(text4)

    input("Press enter to go to sleep...")

    print("...")

    print(text5)

    wallet = getPaid(wallet)

    print("You now have " + str(wallet) + " gold.")

    input("Press enter to travel into the forest...")

    print ()

    print(text6)

    wallet = getPaid(wallet)

    print ("You now have " +str(wallet) + " gold.")

    input("Press enter to continue on...")

    print ()

    print (text7)

    wallet = getPaid(wallet)

    print ("You now have " +str(wallet) + " gold.")

    print ()

    print (text8)

    print ("To be continued...")           
main()

#copyright Christopher Rogers 2020
