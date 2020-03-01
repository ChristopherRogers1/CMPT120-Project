def visitLocale(locale, score, prompt):
    print(locale)
    print("Score: ", score)
    input(prompt)
    print()

def getPaid(wallet):
    return 10 + wallet

def printInfo(location, money):
    print ("Current location: " + location + " Current gold: " +str(money))

def copyright():
    print ("Copyright Christopher Rogers 2020")

def startGame():

    print()
    print("---------------------------")
    print("Welcome to THE HEROIC TALE!")
    print("---------------------------")
    print()
    
    text1 = "Let's start with some information about yourself, traveler. What is your name?"
    print(text1)
    name = input("")
    
    text2 = "Welcome to Eawrsa, " + name + ". Remind me, where do you come from?"
    print(text2)
    home = input("")

    text3 = "Interesting. Only one more question, what was your profession in your homeland?"
    print(text3)
    job = input("")
    print("Ah yes, " + name + ", the great " + job + " of " + home + ".")

    area1 = "It's getting late, and you've got a long day ahead of you; why not take a nap?"
    
    return name, home, job

def gameLoop(location, money, coord1, coord2):
    #coord1 = x, coord2 = y
    areaList = ["You awake to a fire! Your home is burning down! In a panic, you run to the exit, leaving behind all of your money and belongings. The town is being pillaged by the badguyians to the north! You run to the east, towards the woods. Once you arrive, you find a crisp ten dollar coin. Sweet!", 
                "You travel deeper into the forest, leaving your burning town behind. As you travel, you wander across one of your neighbors. 'Thank godness it's you!', they exclaim. They offer you 10 coins in exchange for helping them gather food. You agree, and become 10 coins richer.",
                "You eventually make your way out of the deep forest to be met by a crude gravel road. You travel down the road away from your destroyed home, and eventually come across a lone figure. He is wearing the armor of the northerners which attacked your home. In a fit of rage, you rush him and throw a punch, which somehow luckily connects with a vital organ, killing him instantly. You loot his body, taking what money he had on him.",
                "You make it to a large field, with rolling hills as far as the eye can see. You climb one of the hills, only to figure out that it was an illusion and the hills end there.",
                "You come across a great castle. You approach the entrance, only to find out that it is the fortress of the badguyians! You hide in a nearby bush, and run away when you think nobody is looking.",
                "You return to your burning town. The attackers seem to have left, and did not leave much of anything still standing."]
    currentLocation = location
    
    printInfo(location, money)

    
    
    while (1):
        command = input("Enter a command (North, South, East, West, Help, and Quit): ")
        if (command.lower() == "north"):
            if (coord1!=0 or coord2 == 1):
                print("You cannot travel this way.")
            elif (coord2+1==0):
                return areaList[5], coord1, coord2 + 1;
            else:
                return areaList[1], coord1, coord2 + 1;
        elif (command.lower() == "south"):
            if (coord1!=0 or coord2 == -1):
                print("You cannot travel this way.")
            elif (coord2-1==0):
                return areaList[5], coord1, coord2 - 1;
            else:
                return areaList[3], coord1, coord2 - 1;
        elif (command.lower() == "east"):
            if (coord2!=0 or coord1 == 1):
                print("You cannot travel this way.")
            elif (coord1+1==0):
                return areaList[5], coord1 + 1, coord2;
            else:
                return areaList[2], coord1 + 1, coord2;
        elif (command.lower() == "west"):
            if (coord2!=0 or coord1 == -1):
                print("You cannot travel this way.")
            elif (coord1-1==0):
                return areaList[5], coord1 - 1, coord2;
            else:
                return areaList[4], coord1 - 1, coord2;
        elif (command.lower() == "help"):
            print("Valid commands include North, South, East, West, Help, and Quit.")
        elif (command.lower() == "quit"):
            return "done", 0, 0
        else:
            print("Invalid command, try again")

def main():

    areaList = ["You awake to a fire! Your home is burning down! In a panic, you run to the exit, leaving behind all of your money and belongings. The town is being pillaged by the badguyians to the north! You run to the east, towards the woods. Once you arrive, you find a crisp ten dollar coin. Sweet!", 
                "You travel deeper into the forest, leaving your burning town behind. As you travel, you wander across one of your neighbors. 'Thank godness it's you!', they exclaim. They offer you 10 coins in exchange for helping them gather food. You agree, and become 10 coins richer.",
                "You eventually make your way out of the deep forest to be met by a crude gravel road. You travel down the road away from your destroyed home, and eventually come across a lone figure. He is wearing the armor of the northerners which attacked your home. In a fit of rage, you rush him and throw a punch, which somehow luckily connects with a vital organ, killing him instantly. You loot his body, taking what money he had on him.",
                "You make it to a large field, with rolling hills as far as the eye can see. You climb one of the hills, only to figure out that it was an illusion and the hills end there.",
                "You come across a great castle. You approach the entrance, only to find out that it is the fortress of the badguyians! You hide in a nearby bush, and run away when you think nobody is looking.",
                "You return to your burning town. The attackers seem to have left, and did not leave much of anything still standing."]

    prompt = "Press enter to continue."
        
    name, home, job = startGame()
    
    wallet = 0

    current = areaList[0]

    newLocation, coord1, coord2 = gameLoop(areaList[0], wallet, 0, 0)

    print()

    
    while (newLocation != "done"):
        wallet = getPaid(wallet)
        newLocation, coord1, coord2 = gameLoop(newLocation, wallet, coord1, coord2)
        print()

    
    
    print ("After a long day of traveling, you lay down your head and rest. Who knows what lay ahead of you?")

    print ("To be continued...")

    copyright()
main()
