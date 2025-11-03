# Hangman game (with hints and play-again option)
import random

# Words and matching hints
words = [
    "python", "java", "javascript", "html", "css", "sql", "kotlin", "swift", "ruby", "rust",
    "apple", "banana", "tiger", "elephant", "mountain", "river", "teacher", "doctor",
    "computer", "mobile", "internet", "planet", "school", "garden", "camera", "music", "pizza"
]
hints = [
    "programming language", "programming language", "web scripting language", "web markup", "style sheet language",
    "database query language", "android coding language", "apple app language", "gem-named language", "systems language",
    "a fruit", "a yellow fruit", "a wild animal", "a large animal", "high landform", "flowing water", "educates students",
    "treats patients", "electronic device", "handheld device", "global network", "celestial body", "place of learning",
    "area with plants", "used for photos", "art of sound", "favorite food"
]

def chooseWordAndHint(words, hints):
    idx = random.randrange(len(words))
    return words[idx], hints[idx]

def isWordGuessed(secretWord, lettersGuessed):
    for ch in secretWord:
        if ch not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    ans = ""
    for ch in secretWord:
        if ch in lettersGuessed:
            ans += ch
        else:
            ans += "_ "
    return ans

def hangman(secretWord, hint):
    print("\nWelcome to Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("Hint:", hint)

    lettersGuessed = []
    mistakesMade = 0
    totalChances = 8

    while totalChances - mistakesMade > 0:
        print("-------------")
        print("Word:", getGuessedWord(secretWord, lettersGuessed), "   Hint:", hint)
        print("You have", totalChances - mistakesMade, "guesses left.")

        guess = input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif (len(guess) == 1) and (guess.isalpha()) and (guess in secretWord):
            lettersGuessed.append(guess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            if len(guess) == 1 and guess.isalpha() and (guess not in lettersGuessed):
                lettersGuessed.append(guess)
            mistakesMade += 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))

        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("🎉 Congratulations, you won! 🎉")
            print("The correct word was:", secretWord)
            print("Hint:", hint)
            break

    if not isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("💀 Sorry, you ran out of guesses.")
        print("The correct word was:", secretWord)
        print("Hint:", hint)

# Main game loop with replay feature
while True:
    secretWord, hint = chooseWordAndHint(words, hints)
    hangman(secretWord, hint)

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing Hangman! Goodbye!")
        break
