import random
import time
print('Code go BRRRRRRRR')
plrName = input("What is your name? ")
print('Hi ')
print(plrName)

print('Now for your race')
def GetRace():
    print('You can Use')
    print('Grimlin, Scavenger, Alien')
    plrRace = input("What is your race? ")
    if plrRace == "Grimlin" or plrRace == "Scavenger" or plrRace == "Alien":
        print("Player stats")
        print("Player name")
        print(plrName)
        print("Player Race")
        print(plrRace)
        time.sleep(5)
        print("A monster Found you! Fight!")
        myList = ["You got bitten ", "Killed it but Got a bite","You Killed it"]
        print(random.choice(myList))
        time.sleep(10) 
        print("Player stats")
        print("Player name")
        print(plrName)
        print("Player Race")
        print(plrRace)
        print("Player Health")
        print("44/50")
        print("You adventure around and Find some Nuts and berries")
        print("You Eat them and gain 6 health")
        time.sleep(220)
        print("Game is now closeing")
    else:
        print("Sorry, but that race is not valid")
        GetRace()
GetRace()

