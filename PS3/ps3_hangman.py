# 6.00 Problem Set 3
# 
# Hangman game
#


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    n=0
    while n<len(secretWord):
        x=secretWord[n:n+1]
        if x in lettersGuessed:
              n=n+1
        else:
              return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    n=0
    result=''
    while n<len(secretWord):
        x=secretWord[n:n+1]
        if x in lettersGuessed:
           result=result+x
           n=n+1
        else:
           result=result+' _ '
           n=n+1
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    x=string.ascii_lowercase
    
    for char in lettersGuessed:
        x=x.replace(char,'')
    return x

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    x=len(secretWord)
    print "Welcome to the game, Hangman!"
    one="I am thinking of a word that is " + str(x) + " letters long."
    print one

    mistakesMade=0
    lettersGuessed=[]
        
    while mistakesMade<8:
        print '-----------'
        two= "You have " + str(8-mistakesMade) + " guesses left."
        print two
        availableLetters=getAvailableLetters(lettersGuessed)
        three= "Available letters: "+availableLetters
        print three
        guess = raw_input("Please guess a letter:")
        letter = guess.lower()

        if letter in secretWord and letter not in lettersGuessed:
            lettersGuessed.insert(0,letter)
            y=getGuessedWord(secretWord,lettersGuessed)
            print "Good guess:"+y
            if isWordGuessed(secretWord,lettersGuessed):
                print '-----------'
                z="Congratulations, you won!"
                return z   

        elif letter in lettersGuessed:
            y=getGuessedWord(secretWord,lettersGuessed)
            print "Oops! You've already guessed that letter:"+y

        elif letter not in secretWord:
            lettersGuessed.insert(0,letter)
            y=getGuessedWord(secretWord,lettersGuessed)
            print "Oops! That letter is not in my word:"+y
            mistakesMade=mistakesMade+1

    print '-----------'

    last= "Sorry, you ran out of guesses. The word was"+secretWord
    return last

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
