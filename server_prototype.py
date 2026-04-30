import socket
import random
import json
import re
import requests

HOST = "localhost"
PORT = 5555

def get_wiki():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    headers = {"User-Agent": "HangmanProject/1.0"}

    data = requests.get(url, headers=headers).json()
    return data["title"].lower()

def init_display(word):
    return ["_" if c.isalpha() else c for c in word]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print("Waiting for players...")
p1, addr1 = server.accept()
print("Player 1 connected")

p2, addr2 = server.accept()
print("Player 2 connected")

word = get_wiki()
display = init_display(word)

scores = {
    "p1": 0,
    "p2": 0
}

players = [p1, p2]
names = ["p1", "p2"]

turn = 0

while "_" in display:
    player = players[turn % 2]
    name = names[turn % 2]

    # send state
    msg = json.dumps({
        "display": display,
        "score": scores,
        "your_turn": name
    })
    player.send(msg.encode())

    # receive guess
    guess = player.recv(1024).decode().lower()

    if guess not in word:
        scores[name] += 1

    # update display
    for i, c in enumerate(word):
        if c == guess:
            display[i] = guess

    turn += 1

result = json.dumps({
    "final_word": word,
    "scores": scores
})

p1.send(result.encode())
p2.send(result.encode())

p1.close()
p2.close()
server.close()
