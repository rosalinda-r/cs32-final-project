from socket32 import create_new_socket
import json

client = create_new_socket()
client.connect("127.0.0.1", 6666)

data = json.loads(client.recv())
word = data["word"]


display = [
    "_" if char.isalpha() else char
    for char in word
]

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

guessed = []
wrong = 0

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
        break

    else:
        wrong += 1
        print("Wrong guess!")

if "_" not in display:
    print("\nYou won! The word was", word)
else:
    print(hangman_stages[wrong])
    print("\nYou lost! The word was", word)

client.sendall(json.dumps({
    "wrong": wrong
}))
