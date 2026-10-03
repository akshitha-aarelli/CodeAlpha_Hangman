# CodeAlpha Internship - Task 1: Hangman Game
import random

WORDS = ["python", "internship", "developer", "keyboard", "program"]
MAX_WRONG = 6


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("\n=== HANGMAN ===")
    print("Guess the word one letter at a time.")
    print(f"You can make {MAX_WRONG} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("Word:", display)

        if "_" not in display:
            print("\nCongratulations! You won! The word was:", word)
            return

        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "none")
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    print("Game over! You lost. The word was:", word)


def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing!")
            break


main()