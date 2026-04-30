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

def get_book():
    url = "https://www.googleapis.com/books/v1/volumes?q=fiction"
    data = requests.get(url).json()

    if "items" not in data:
        return "harry potter"

    books = data["items"]
    book = random.choice(books)
    return book["volumeInfo"]["title"].lower()

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
        return "blank space"

    song = random.choice(data["results"])
    return song["trackName"].lower()

def choose_mode():
    while True:
        mode = input("Choose mode (wiki/book/song): ").lower()

        if mode in ["wiki", "book", "song"]:
            return mode

        print("Invalid mode. Please enter: wiki, book, or song.\n")


# 🧑‍🤝‍🧑 NEW: player names
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

mode = choose_mode()

if mode == "song":
    word = get_song()
elif mode == "book":
    word = get_book()
else:
    word = get_wiki()

display = [
    "_" if char.isalpha() else char
    for char in word
]

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

guessed = []
wrong = 0

# 🧑‍🤝‍🧑 NEW: player tracking
player1_guesses = []
player2_guesses = []
player1_count = 0
player2_count = 0

current_player = 1
winner = None

print("Welcome to Multiplayer Hangman!")

while wrong < 6 and "_" in display:
    print(hangman_stages[wrong])
    print("Word:", " ".join(display))
    print("All guessed letters:", " ".join(guessed))
    print(f"{player1}'s guesses:", " ".join(player1_guesses))
    print(f"{player2}'s guesses:", " ".join(player2_guesses))
    print()

    # 🧑‍🤝‍🧑 whose turn
    if current_player == 1:
        player_name = player1
        player_list = player1_guesses
    else:
        player_name = player2
        player_list = player2_guesses

    print(f"{player_name}'s turn")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one valid letter.\n")
        continue

    if guess in guessed:
        print("You already guessed that.\n")
        continue

    guessed.append(guess)
    player_list.append(guess)

    # 🧑‍🤝‍🧑 track counts
    if current_player == 1:
        player1_count += 1
    else:
        player2_count += 1

    if guess in [c for c in word if c.isalpha()]:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Good guess!\n")

        # 🧑‍🤝‍🧑 check winner
        if "_" not in display:
            winner = player_name
            break
    else:
        wrong += 1
        print("Wrong guess!\n")

    # switch player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1


# 🧾 FINAL SUMMARY
print("\n===== GAME SUMMARY =====")
print("Final word:", word)
print("Final board:", " ".join(display))
print()

print(f"{player1}: {player1_count} guesses")
print("Letters guessed:", " ".join(player1_guesses))
print()

print(f"{player2}: {player2_count} guesses")
print("Letters guessed:", " ".join(player2_guesses))
print()

if winner:
    if winner == player1:
        print(f"{player1}, you won!")
        print(f"{player2}, you lost!")
    else:
        print(f"{player2}, you won!")
        print(f"{player1}, you lost!")
else:
    print("Both players lost!")
