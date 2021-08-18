"""
Created on Wed Aug 18 08:25:19 2021

@author: Jordan Kennedy (Twitter: @imjorman)
"""
import random

def play(userInput, computerInput):
    if userInput == computerInput:
        print("It's a tie!")
    elif userInput == "rock" and computerInput == "paper":
        print("Paper covers rock.  You lose!")
        return "computer"
    elif userInput == "paper" and computerInput == "scissors":
        print("Scissors cut paper.  You lose!")
        return "computer"
    elif userInput == "scissors" and computerInput == "rock":
        print("Rock crushes scissors.  You lose!")
        return "computer"
    else:
        print("You win!  Congratulations!")
        return "human"

def computerPick():
    randomNum = random.randint(0, 2)
    
    if randomNum == 0:
        return "rock"
    elif randomNum == 1:
        return "paper"
    else:
        return "scissors"
    

playerScore = 0
computerScore = 0


playing = True

print("Hello!  What is your name?", end = "")
playerName = input()
print()

print(f'Hi {playerName}.  Do you want to play rock, paper, scissors? (yes/no)', end="")
wantToPlay = input().lower()
if wantToPlay == "no":
    print("Goodbye")
    playing = False
print()

while playing == True:
    winner = "computer"
    
    print("It's time to play.  Pick rock, paper, or scissors.", end="")
    userChoice = input().lower()
    print()
    
    computerChoice = computerPick()
    print(f"The computer chose {computerChoice}.", end= " ")
    
    winner = play(userChoice, computerChoice)
    print()
    if winner == "computer":
        computerScore += 1
    elif winner == "human":
        playerScore += 1
      
    print(f"The current score is {playerName}: {playerScore} and Computer: {computerScore}.")
    print("Play again? (yes/no)", end ="")
    playAgain = input().lower()
    print()
    if playAgain == "no":
        print("Goodbye")
        playing = False
    else:
        continue
