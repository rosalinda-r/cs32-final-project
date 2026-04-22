import random

words = ["apple", "tiger", "python", "school", "planet"]

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

word = random.choice(words)
guessed = []
wrong = 0
display = ["_"] * len(word)

print("Welcome to Hangman!")

while wrong < 6 and "_" in display:
    print(hangman_stages[wrong])
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one valid letter.")
        continue

    if guess in guessed:
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Good guess!")
    else:
        wrong += 1
        print("Wrong guess!")

if "_" not in display:
    print("\nYou won! The word was", word)
else:
    print(hangman_stages[wrong])
    print("\nYou lost! The word was", word)
