##Single Player Hangman Game
import random
##Create Words List
words = ['cosmo', 'wanda', 'waldo', 'odlaw', 'cat', 'hat', 'tuple', 'roshambo', 'list', 'coarsen']
def main():
    print('## WELCOME TO HANGMAN! ## \nPress ENTER to START')
# Pick a random word

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display word with blanks
display_word = ["_"] * len(word)

print("Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in display_word:
    print("\nWord: " + " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong!")
        wrong_guesses += 1

# End of game
if "_" not in display_word:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
