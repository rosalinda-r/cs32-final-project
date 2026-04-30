import requests
import random
def get_wiki():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

    headers = {
        "User-Agent": "HangmanProject/1.0 (student project)"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    title = data["title"]
    return title.lower()

###NEW CODE
def get_tv():
    url = "https://api.tvmaze.com/shows"

    response = requests.get(url)
    data = response.json()

    show = random.choice(data)
    title = show["name"].lower()

    return title

def get_song():
    url = "https://itunes.apple.com/search"

    params = {
        "term": "music",
        "media": "music",
        "entity": "song",
        "limit": 50
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return "blank space"  # fallback

    song = random.choice(data["results"])
    return song["trackName"].lower()

def choose_mode():
    while True:
        mode = input("Choose mode (wiki/book/song): ").lower()

        if mode in ["wiki", "tv", "song"]:
            return mode

        print("Invalid mode. Please enter: wiki, tv, or song.\n")

mode = choose_mode()

if mode == "song":
    word = get_song()

elif mode == "tv":
    word = get_tv()
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
