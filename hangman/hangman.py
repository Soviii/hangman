import os
import string
from extra import hangmanArt

os.system('cls')

def printLayout(hangmanArtCounter, progress, entries):
    print(str(progress).strip('[]').replace(',', '').replace('\'',''))
    print(hangmanArt[hangmanArtCounter])
    entries = str(entries).strip('[]').replace('\'', '')
    print(f'You have tried - {entries}')

word = "so"
chosenWord = list(word)
progress = []
hangmanArtCounter = 0
userChar = ''
entries = []
winStatus = False

for _ in range(len(chosenWord)):
    progress.append('_')

while hangmanArtCounter < len(hangmanArt)-1: 
    printLayout(hangmanArtCounter, progress, entries)
    userChar = input('Enter a letter \t')
    if len(userChar) != 1:
        print('You have entered the wrong number of characters, please try again.')
    elif userChar not in string.ascii_lowercase:
        print('You have entered an invalid input. Only enter lowercase letters.')
    else:
        if userChar in chosenWord:
            if userChar in progress:
                print('You have already guessed that letter')
                continue
            else: 
                for index, char in enumerate(chosenWord):
                    if char == userChar:
                        progress[index] = char
                entries.append(userChar)
                if progress == chosenWord:
                    winStatus = True
                    break
        elif userChar in entries:
            print('You have already tried that letter')
        else:
            hangmanArtCounter += 1
            entries.append(userChar)
            print('Letter is not here, try again')


os.system('cls')
if winStatus:
    printLayout(hangmanArtCounter, progress, entries)
    print('Good job')
else:
    printLayout(hangmanArtCounter, progress, entries)
    print(f'The word was - {word}. Nice try')