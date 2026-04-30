from socket32 import create_new_socket
import json

server = create_new_socket()
server.bind("127.0.0.1", 5555)
server.listen()

print("Waiting for players...")
p1, addr1 = server.accept()
p2, addr2 = server.accept()

print("Players connected!")

word = "hello world"  # later replace with wiki/book/song
display = ["_" if c.isalpha() else c for c in word]

scores = {"p1": 0, "p2": 0}
turn = 0

players = [p1, p2]

while "_" in display:
    current = players[turn % 2]
    player_name = "p1" if turn % 2 == 0 else "p2"

    # send state
    current.sendall(json.dumps({
        "display": display,
        "scores": scores,
        "your_turn": player_name
    }))

    guess = current.recv().lower()

    if guess not in word:
        scores[player_name] += 1
    else:
        for i, c in enumerate(word):
            if c == guess:
                display[i] = guess

    turn += 1

result = {
    "final_word": word,
    "scores": scores
}

p1.sendall(json.dumps(result))
p2.sendall(json.dumps(result))
