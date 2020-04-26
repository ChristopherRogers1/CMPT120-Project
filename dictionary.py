def main():
    
    print("Input Filename (do not include .txt): ")
    
    fileName = input("") + ".txt"

    dictionary = {}
    counter = 0
    temp = "temp"
    repeat = 1
    
    with open(fileName, 'r') as file:
        for line in file:
            if counter%2==0:
                temp = line.rstrip("\n")
            else:
                dictionary[temp] = line.rstrip("\n")
            counter += 1    

    for x in dictionary:
        print(x)

    while (repeat == 1):
        
        inputWord = input("Enter the word you'd like to find: ").lower()
        if inputWord in dictionary:
            print (dictionary[inputWord])
        elif (inputWord == ""):
            repeat = 0
        else:
            print("Word not found, try again")
main()
