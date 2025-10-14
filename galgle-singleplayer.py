import pyfiglet
import os
from random_word import RandomWords

r = RandomWords()
word = ""
while len(word) < 4:
    word = r.get_random_word()
os.system('cls' if os.name == 'nt' else 'clear')    # clears screen
wordlength = len(word)
dotline = "_" * wordlength      # Makes a line for the letters to be filled in
correct = False
guessedLetters = set()          # Creates an empty set for incorrectly guessed letters 

mistakes = 0
print(f"{wordlength} letters. You can make 7 mistakes.")
print(dotline)

while correct == False:                                 # Main game loop

    guess = input("Guess a letter: ")                   # Listens for input and
    os.system('cls' if os.name == 'nt' else 'clear')    # clears screen
    wrong_guess = True

    for position in range(0, wordlength):
        currentLetter = word[position]
        if str(currentLetter) == str(guess):                                        # Checks if guessed letter is the word's letter in nth position
            dotline = dotline[:position] + currentLetter + dotline[position+1:]     # Replaces underscore by correct letter
            wrong_guess = False                                                     # Updates wrong_guess so no mistakes are counted

    if wrong_guess == True:
        mistakes += 1                   # Counts mistake
        guessedLetters.add(guess)       # Adds letter to incorrect guesses


# Print results and hangman
    print("")
    print(f"{dotline}   Mistakes: {mistakes}/7")
    if mistakes == 0:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    elif mistakes == 1:
        print("")
        print("|")
        print("|")
        print("|")
        print("|")
        print("")
    elif mistakes == 2:
        print("_____")
        print("|")
        print("|")
        print("|")
        print("|")
        print("")
    elif mistakes == 3:
        print("_____")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("")
    elif mistakes == 4:
        print("_____")
        print("|   |")
        print("|   O")
        print("|")
        print("|")
        print("")
    elif mistakes == 5:
        print("_____")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|")
        print("")
    elif mistakes == 6:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|")
        print("")
    elif mistakes == 7:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  / \\")
        print("")

# Print guessed letters
    print("Guessed letters: "+", ".join(map(str, guessedLetters)))
    print("")

# Checks win/lose conditions
    if mistakes > 6:
        print()
        print(pyfiglet.figlet_format(" YOU", font="sblood"))
        print(pyfiglet.figlet_format("LOSE", font="poison"))
        print(f"The word was: '{word}'")
        break
    elif dotline == word:
        correct = True
        print(pyfiglet.figlet_format("WELL DONE!", font="univers"))