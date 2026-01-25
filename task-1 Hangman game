import random

words = ["python", "hangman", "computer", "program", "college"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")


while wrong_guesses < max_wrong:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

   
    if guess in word:
        print(" Good guess!\n")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Remaining attempts: {max_wrong - wrong_guesses}\n")

if wrong_guesses == max_wrong:
    print("Game Over!")
    print("The word was:", word)
