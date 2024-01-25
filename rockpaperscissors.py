from random import randrange
import time

typeArray = ["ROCK", "PAPER", "SCISSORS"]
totalPlayerPoints = 0
totalComputerPoints = 0




def generateValue():
    generatedValue = randrange(3)
    return generatedValue




def generateComputerTalkOne():
    print("ROCK!")
    time.sleep(0.5)
    print("PAPER!")
    time.sleep(0.5)
    print("SCISSORS!")
    time.sleep(0.5)
    print("SHOOT! \n")
    print("           . . .           ")




def playOneGame():

    global totalPlayerPoints
    global totalComputerPoints

    inputValue = str(input("\nComputer asks 'ROCK, PAPER, OR SCISSORS?'\nEnter Answer Here: "))
    generateComputerTalkOne()
    computerValue = typeArray[generateValue()]

    # SCENARIOS WHERE THE PLAYER WINS:
    if inputValue == computerValue:
        print("Draw")
    elif inputValue == typeArray[0] and computerValue == typeArray[2]: #ROCK BEATS SCISSORS (POINT TO PLAYER)
        print("Computer chose " + typeArray[2] + "\nYou win!")
        totalPlayerPoints += 1
    elif inputValue == typeArray[1] and computerValue == typeArray[0]: #PAPER BEATS ROCK (POINT TO PLAYER)
        print("Computer chose " + typeArray[0] + "\nYou win!")
        totalPlayerPoints += 1
    elif inputValue == typeArray[2] and computerValue == typeArray[1]: #SCISSORS BEATS PAPER (POINT TO PLAYER)
        print("Computer chose " + typeArray[1] + "\nYou win!")
        totalPlayerPoints += 1

    # SCENARIOS WHERE THE PLAYER LOSES:
    elif inputValue == typeArray[0] and computerValue == typeArray[1]: #PAPER BEATS ROCK (POINT TO COMPUTER)
        print("Computer chose " + typeArray[1] + "\nYou lost...")
        totalComputerPoints += 1
    elif inputValue == typeArray[1] and computerValue == typeArray[2]: #SCISSORS BEATS PAPER (POINT TO COMPUTER)
        print("Computer chose " + typeArray[2] + "\nYou lost...")
        totalComputerPoints += 1
    elif inputValue == typeArray[2] and computerValue == typeArray[0]: #ROCK BEATS SCISSORS (POINT TO COMPUTER)
        print("Computer chose " + typeArray[0] + "\nYou lost...")
        totalComputerPoints += 1
    else:
        print("PLEASE INPUT A VALID INPUT")

    print("           . . .           ", "\nYour Points: ", totalPlayerPoints, "\nThe Computer's Points: ", totalComputerPoints, "\n           . . .           ")




def playAGame():
    global totalPlayerPoints
    global totalComputerPoints

    totalPlayerPoints = 0
    totalComputerPoints = 0
    totalPoints = totalComputerPoints + totalPlayerPoints

    print("[WELCOME TO ROCK, PAPER, AND SCISSORS!]")

    while totalPlayerPoints + totalComputerPoints < 3:
        playOneGame()

    print("[Game Over]")

    if totalPlayerPoints > totalComputerPoints:
        print("You win!")
    elif totalPlayerPoints < totalComputerPoints:
        print("You lose!")
    else:
        print("It's a draw!")





playAGame()


