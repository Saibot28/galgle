import pyfiglet
import os
import pwinput

word = pwinput.pwinput("Enter the word: ").lower()
os.system('cls' if os.name == 'nt' else 'clear')
itr = 0
wordlength = len(word)
dotline = "_" * wordlength
correct = False
guessedLetters = set()

mistakes = 0
print(f"{wordlength} letters. You can make 7 mistakes.")
print(dotline)

while correct == False:

    guess = input("Guess a letter: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    wrong_guess = True

    for position in range(0, wordlength):
        currentLetter = word[position]
        if str(currentLetter) == str(guess):
            dotline = dotline[:position] + currentLetter + dotline[position+1:]
            wrong_guess = False

    if wrong_guess == True:
        mistakes += 1
        guessedLetters.add(guess)


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

    print("Guessed letters: "+", ".join(map(str, guessedLetters)))
    print("")

    if mistakes > 6:
        print()
        print(pyfiglet.figlet_format(" YOU", font="sblood"))
        print(pyfiglet.figlet_format("LOSE", font="poison"))
        print(f"The word was: '{word}'")
        break
    elif dotline == word:
        correct = True
        print(pyfiglet.figlet_format("WELL DONE!", font="univers"))