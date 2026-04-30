import re
import requests
def get_wiki():
    # Get a random Wikipedia page
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

    headers = {
        "User-Agent": "HangmanProject/1.0 (student project)"
    }

    response = requests.get(url, headers=headers)
    # Extract the title and store it in 'title'
    data = response.json()
    title = data["title"]
    word = title.lower()

###NEW CODE
def get_book():

    url = "https://www.googleapis.com/books/v1/volumes?q=fiction"
    data = requests.get(url).json()

    books = data["items"]
    word = books[0]["volumeInfo"]["title"].lower()

mode = input("Choose mode: ")
'''
if mode == "movie":
    word = get_movie()
elif mode == "song":
    word = get_song()
'''
if mode == "book":
    word = get_book()
else:
    word = get_wiki()
####

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
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess in [c for c in word if c.isalpha()]:
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
