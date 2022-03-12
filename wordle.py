#import random to select random word from the list
from operator import pos
import random

#define a function to check the letters and give clues
def processguess(theAnswer, theGuess):
    position = 0
    clue = ""
    for letter in theGuess:
        if letter == theAnswer[position]:
         
            clue += "()"

        elif letter == theAnswer:
            clue += '{}'
        else:
            clue += "-"
            position += 1
    print(clue)
    return clue == "()()()()()"

#Load the words onto the list
word_list = ["APPLE", "WEARY", "PILLS", "VAGUE"]

#snippet to randomly choose a word from the list
answer = random.choice(word_list)

#the variables to determine the guesses and the guessed words
num_of_guesses = 0
guess_correct = False

#use the while loop to check the conditions of the game
while num_of_guesses < 6 and not guess_correct:
    #prompt user to enter their guess
    guess = input("Input your guess:  ")
    print("Your Guess is " +guess)
    num_of_guesses += 1
    

    #process guesses
    guess_correct = processguess(answer, guess)


#print the game messages
if guess_correct:
    print("Congratulations! You won! The Correct word is indeed", answer)
    
else:
    print("Sorry you lost...The correct word is " ,answer)
