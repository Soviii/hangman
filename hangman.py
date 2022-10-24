import os
import string
from extra import hangmanArt
import random
os.system('cls') # clears terminal

# another way of keeping comments is by using 6 apostraphes: 3 in front of comment and after comment
"""Helper function for printing layout when running main driver of code"""
"""Keeps track of which hangman picture to print when called along with printing the different 
   entries people have entered"""
def printLayout(hangmanArtCounter, progress, entries):
    print(str(progress).strip('[]').replace(',', '').replace('\'',''))
    print(hangmanArt[hangmanArtCounter])
    entries = str(entries).strip('[]').replace('\'', '')
    print(f'You have tried - {entries}')


# holds possible words for hangman game
wordBank = ['elephant', 'tiger', 'flamingo', 'panda', 'porcupine', 'eagle', 'tarantula', 'seagull', 'dolphin', 'whale', 'woodpecker', 'chicken', 'horse', 'pelican'] # word bank of possible words; can add or remove words to programmer's discretion
word = random.choice(wordBank)
chosenWord = list(word) # breaks up word into separate letters as each element EX: 'tiger' -> ['t', 'i', 'g', 'e', 'r']
progress = [] # player's current progress; only holds correct letters from entries
hangmanArtCounter = 0 # keeping track of what hangman art to use for UI
userChar = '' # holds the user's character for comparison; used for checking valid inputs
entries = [] # both wrong and right letters entered; in case of player entering the same letter again
winStatus = False # holds current status of if the player guessed the word correctly within certain tries

for _ in range(len(chosenWord)):
    progress.append('_')

while hangmanArtCounter < len(hangmanArt)-1:  # user keeps attempting while they haven't reached certain number of tries
    printLayout(hangmanArtCounter, progress, entries) # helper function called
    userChar = input('Enter a letter \t') # prompts user to enter a letter/character
    if len(userChar) != 1: # if user did not enter a character or entered more than 1 character
        print('You have entered the wrong number of characters, please try again.')
    elif userChar not in string.ascii_lowercase: # if user did not enter a lowercase letter
        print('You have entered an invalid input. Only enter lowercase letters.')
    else: # enters 'else' statement only if they entered a lowercase letter
        if userChar in chosenWord: # if userinput is in chosen word
            if userChar in progress: # if userinput is already part of progress; user already entered letter
                print('You have already guessed that letter')
                continue # continue keyword skips all lines and goes to next iteration of loop; goes back to the top when ran
            else: # enters else statement if user input is a new letter and is part of chosen word
                for index, char in enumerate(chosenWord): # each iteration holds the index and the value(char) for code to use
                    if char == userChar: 
                        progress[index] = char # want to update current progress for displaying in UI; puts letter in same index location in progress as chosen word array 
                entries.append(userChar) # add letter to entry history bank
                if progress == chosenWord: # if progress array equals chosen word array, user has won
                    winStatus = True
                    break # breaks out of while loop 
        elif userChar in entries: # if user already guessed that letter
            print('You have already tried that letter')
        else: # if entry is not part of chosen word; penalty
            hangmanArtCounter += 1 # increments for hangman ASCII art
            entries.append(userChar) # adds letter to entry history bank
            print('Letter is not here, try again')


os.system('cls')
if winStatus: # if user won
    printLayout(hangmanArtCounter, progress, entries)
    print('Good job')
else: # if user lost
    printLayout(hangmanArtCounter, progress, entries)
    print(f'The word was - {word}. Nice try')
