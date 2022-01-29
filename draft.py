#Group 20
#Project 1: "Guess-the-letters"
#Main File
#Friday November 15 2019
#Aranya Sutharsan (100748986)
#Rinoa Malapaya (100743955)
#Noshin Rahman (100745332)

import random

#Main Functions - calls all functions
def main():
    global wordLen4
    global wordLen5
    global alphabet
    global attempt
    global terminationWanted
    global correctLetters
    global wrongLetters
    global usedLetters
    global gameFinish
    wordLen4 = []
    wordLen5 = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    attempt = 0
    terminationWanted = False
    correctLetters = ''
    wrongLetters = ''
    usedLetters = ''
    gameFinish = False
    welcomingUser()
    askGuessNum()

def welcomingUser():
    print("Welcome to Guess-the-letters Game")
    print()


#Asks the user the number of guesses
def askGuessNum():
    global numOfGuesses
    numOfGuesses = input("How many guesses you want [1-10]: ")
    verifyGuessValue()


#Sees if user inputs exit/stop then game terminates, if not checks if the input is a number and calls the checkGuessNumRange.
def verifyGuessValue():
    global numOfGuesses
    # global lenOfWord
    # global userGuess
    global terminationWanted
    if numOfGuesses.lower() in ['exit', 'stop']:
        # lenOfWord = ""
        # userGuess = ""
        terminationWanted = True
        askUserToGuess()
    else:
        if numOfGuesses.isdigit():
            checkGuessNumRange()
        else:
            print("Enter a number within the range provided!")
            askGuessNum()


# This function checks if the num of Guess is in the range (0-10)
def checkGuessNumRange():
    global numOfGuesses
    global terminationWanted
    global guessNum
    if numOfGuesses.lower() in ['exit', 'stop']:
        terminationWanted = True
        askUserToGuess()
    else:
        if not numOfGuesses.isdigit():
            verifyGuessValue()
        if numOfGuesses.lower() in ['exit', 'stop']:
            terminationWanted = True
            askUserToGuess()
        else:
            guessNum = int(numOfGuesses)
            if guessNum < 1 or guessNum > 10:
                print("Enter a number within the range provided!")
                askGuessNum()
            else:
                askWordLen()


#Asks the user the length of word
def askWordLen():
    global lenOfWord
    lenOfWord = input("Select the word length [4-5]: ")
    verifyWordlenValue()


#Sees if user inputs exit/stop then game terminates, if not checks if the input is a number and calls the checkWordLenRange
def verifyWordlenValue():
    global lenOfWord
    # global numOfGuesses
    # global userGuess
    global terminationWanted
    if lenOfWord.lower() in ['exit', 'stop']:
        # numOfGuesses = ""
        # userGuess = ""
        terminationWanted = True
        askUserToGuess()
    else:
        if lenOfWord.isdigit():
            checkWordLenRange()
        else:
            print("Invalid input! Please enter a number within range provided")
            askWordLen()

# This function checks if the lenofword is in the range (4 or 5 )
def checkWordLenRange():
    global lenOfWord
    # global numOfGuesses
    # global userGuess
    global terminationWanted
    global wordLen
    if lenOfWord.lower() in ['exit', 'stop']:
        # numOfGuesses = ""
        # userGuess = ""
        terminationWanted = True
        askUserToGuess()
    else:
        if not lenOfWord.isdigit():
            verifyWordlenValue()
        if lenOfWord.lower() in ['exit', 'stop']:
            terminationWanted = True
            askUserToGuess()
        else:
            wordLen = int(lenOfWord)
            if wordLen < 4 or wordLen > 5:
                print("Invalid input! Please enter a number within range provided")
                askWordLen()
            else:
                processingWord()


def processingWord():
    print("Selecting the word...")
    chooseWord()
    encryptWord()


#Chooses word from 'word.txt' file
#Checks if the word length is 4 or 5
#Randomly assigns a word
def chooseWord():
    global wordLen
    global dictFile
    global wordLen4
    global wordLen5
    dictFile = open('words.txt')
    dict = []
    for line in dictFile:
        dict.append(line.strip("\n"))
    for c in dict:
        if len(c) == 4:
            wordLen4.append(c)
        elif len(c) == 5:
            wordLen5.append(c)
    wordPosition = random.randint(0, 4)
    global fixedWord
    if wordLen == 5:
        fixedWord = wordLen5[wordPosition]
    else:
        fixedWord = wordLen4[wordPosition]


#Display
def encryptWord():
    print()
    global encrypted
    global fixedWord
    encrypted = "*" * len(fixedWord)
    print(fixedWord) # ANSWER HERE
    print("Word is:", encrypted)
    askUserToGuess()


def askUserToGuess():
    global userGuess
    global attempt
    global numOfGuesses
    global lenOfWord
    global terminationWanted
    global gameFinish
    global guessesLeft
    global userGuess
    if terminationWanted == True:
        print()
        askToReplay()
        #userGuess = "exit"
        #if userGuess.lower() in ['exit', 'stop']:
            #askToReplay()
        #elif numOfGuesses.lower() in ['exit', 'stop']:
            #askToReplay()
        #elif lenOfWord.lower() in ['exit', 'stop']:
            #askToReplay()
    else:
        notifyUserOfRemainingGuesses()
        checkUserStatus()
        if gameFinish == True or guessesLeft == 0:
            askToReplay()
        else:
            userGuess = input("Choose a letter to guess: ")
            if userGuess.lower() in ['exit', 'stop']:
                terminationWanted = True
                askUserToGuess()
            else:
                verifyUserGuess()
                #showLettersUsed()


def verifyUserGuess():
    global userGuess
    global alphabet
    if len(userGuess) != 1 or userGuess.lower() not in alphabet:
        print(userGuess, "is an invalid input. Please only enter a single character.")
        print()
        print("Word is:", encrypted)
        askUserToGuess()
    else:
        repeatedLetters()


def checkForCorrectLetters():
    global encrypted
    global fixedWord
    global guessesLeft
    global attempt
    for ch in range(len(fixedWord)):  # replace blanks with correctly guessed letters
        if fixedWord[ch] in userGuess:
            encrypted = encrypted[:ch] + fixedWord[ch] + encrypted[ch + 1:]
    # print()
    print("Word:", encrypted)
    askUserToGuess()


def notifyUserOfRemainingGuesses():
    global guessNum
    global initialGuessNum
    global guessesLeft
    # print("Previous Guesses:", usedLetters)
    guessesLeft = guessNum - attempt
    if attempt == 0:
        initialGuessNum = guessNum
        print("Guesses remaining: ", initialGuessNum)
    else:
        print("Guesses remaining: ", guessesLeft)
    print("Previous Guesses:", usedLetters)



def showLettersUsed():
    global correctLetters
    global wrongLetters
    global usedLetters
    global userGuess
    global attempt
    global terminationWanted
    if userGuess.lower() in ['exit', 'stop']:
        terminationWanted = True
        askUserToGuess() # idk
    else:
        if userGuess.lower() in fixedWord and gameFinish == False:
            if not userGuess.lower() in correctLetters:
                print("'" + str(userGuess.lower()) + "' is in the word!")
                print()
                correctLetters = correctLetters + userGuess.lower()
        if not userGuess.lower() in fixedWord and gameFinish == False:
            if not userGuess.lower() in wrongLetters:
                print("'" + str(userGuess.lower()) + "' is NOT in the word! Try again!")
                print()
                wrongLetters = wrongLetters + userGuess.lower()
        usedLetters = wrongLetters
        attempt += 1
        checkForCorrectLetters()


def repeatedLetters():
    global userGuess
    global terminationWanted
    global attempt
    global wrongLetters
    global correctLetters
    if userGuess.lower() in ['exit', 'stop']:
        terminationWanted = True
        askUserToGuess()  # idk
    else:
        if userGuess.lower() in wrongLetters:
            attempt -= 1
            print("'" + str(userGuess.lower()) + "' is NOT in the word and has been guessed before")

            # askUserToGuess()
        if userGuess.lower() in correctLetters:
            attempt -= 1
            print("'" + str(userGuess.lower()) + "' is PRESENT in the word but has been guessed before")
        showLettersUsed()
            # askUserToGuess()


def checkUserStatus():
    global lettersFound
    global gameFinish
    global guessNum
    lettersFound = True
    for i in range(len(fixedWord)):
        if fixedWord[i] not in correctLetters:
            lettersFound = False
    if lettersFound == True:
        print("Congratulations! You won!")
        gameFinish = True

    if lettersFound == False and guessesLeft == 0:
        print("No more guesses left. You lost! Try again next time.")
        print()
        gameFinish = True


def askToReplay():
    global replayOption
    global terminationWanted
    replayOption = input("Do you want to continue Y/N: ")
    verifyReplayInput()


def verifyReplayInput():
    global replayOption
    global terminationWanted
    if not replayOption.isalpha():
        print(replayOption, "is an invalid input. Please do not enter numbers / special characters.")
        askToReplay()
    else:
        if replayOption == "Y" or replayOption == "y":
            print()
            main()
        elif replayOption == "N" or replayOption == "n":
            print()
            if not terminationWanted:
                print("Game ends!")
            else:
                print("You lost! Game ends! Thank you!")
        else:
            print(replayOption, "in an invalid input. Enter Y or N.")
            askToReplay()


main()