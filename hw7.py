# File:        hw7.py
# Written by:  Kyle Fritz
# Date:        11/1/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: This program is a hangman game.
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash

# import the randrange function from the random library
from random import randrange

def printGreeting():
    print("Welcome to Hangman")

# input: Whether or not the player wants to play again.
# output: Whether the boolean is True or False.
def playAgain():
    userPlay = "unsure"
    userPlay = input("Play again? (y or n) ")
    userPlay = userPlay.lower()
    while userPlay != "y" and userPlay != "n":
        userPlay = input("Play again? (please type y or n) ")
        userPlay = userPlay.lower()
    if userPlay == "y":
        return True
    elif userPlay == "n":
        return False

# input: The word and the correct letters already inputted by the user.
# output: Whether or not the user has won the game.
def wonGame(correctLetters, secretWord):
    boolean = False
    secretWord = list(secretWord)
    b = []
    for char in secretWord:
        if char in correctLetters:
            # a is the characters in secretWord.
            a = char
            # b will have the same list of characters as a. 
            b.append(a)
        if b == secretWord:
            word = "".join(secretWord)
            print("You won! The word is", word)
            boolean = True
    return boolean

# input: How many wrong guesses the user has
# output: Whether or not the user has lost the game
def lostGame(numMissedLetters):
    boolean = False
    if numMissedLetters <= 0:
        print("Sorry, better luck next time.")
        boolean = True
    return boolean    
        

# input: a list of all guessed letters
# output: A guess is chosen by the user
def getGuess(allGuessedLetters):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    guess = ""
    # This makes sure that the guess is valid
    while len(guess) != 1 or guess in allGuessedLetters or guess not in alpha:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("You must enter a single letter.")
        elif guess in allGuessedLetters:
            print("You already guessed that letter.")
        elif guess not in alpha:
            print("Please enter a LETTER.")
    allGuessedLetters.append(guess)        
    return guess        

# input: Important information about the game (guesses left, the word, correct
#     letters)
# output: Displays what is currently happening during that hangman turn
def displayTurn(numMissedLetters, correctLetters, secretWord):
    secretWord = list(secretWord)
    # This prints what letters are correct, as well as leaves the other spaces
    #   blank.
    for char in secretWord:
        if char in correctLetters:
            print(char, end = " ")
        else:
            print("_", end = " ")
    print("  incorrect guesses left:", numMissedLetters)
    print()

# input: The words from the file
# output: Keeps the game going until user wins or loses
def playGame(words):
    word = getRandomWord(words)
    secretWord = word.lower()
    numMissedLetters = 5
    correctLetters = []
    allGuessedLetters = []
    boolean = False
    displayTurn(numMissedLetters, correctLetters, secretWord)
    while boolean == False:
        guess = getGuess(allGuessedLetters)
        if guess in secretWord:
            print("Yes, there's a", guess)
            correctLetters.append(guess)
        elif guess not in secretWord:
            print("Sorry, no", guess)
            numMissedLetters -= 1    
        displayTurn(numMissedLetters, correctLetters, secretWord)
        boolean = wonGame(correctLetters, secretWord)
        if boolean == False:
            boolean = lostGame(numMissedLetters)

# input: Words from the file
# output: A random word from the words is chosen
def getRandomWord(words):
    word = randrange(0, len(words))
    return words[word]

# input: file inputted by user in main
# output: list of all words in file
def readWords(fileName):
    readFile = open(fileName, "r")
    firstLine = readFile.readline()
    secondLine = readFile.readline()
    thirdLine = readFile.readline()
    fourthLine = readFile.readline()
    listWords = list(firstLine.split() + secondLine.split())
    listWords = list(listWords + thirdLine.split() + fourthLine.split())
    return listWords

def main():
    printGreeting()
    validation = False
    while validation == False:
        try:
            userFile = input("Enter the file name that's holding the words: ")
            readFile = open(userFile, "r")
            validation = True
        except(FileNotFoundError):
            print("Please choose a valid file.")
    words = readWords(userFile)
    boolean = True
    while boolean == True:
        playGame(words)
        boolean = playAgain()
    
main()
