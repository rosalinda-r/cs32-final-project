from socket32 import create_new_socket
import json

server = create_new_socket()
server.bind("127.0.0.1", 5555)
server.listen()

print("Waiting for players...")

p1, _ = server.accept()
p2, _ = server.accept()

word = "hello world"  # replace with wiki/book/song

p1.sendall(json.dumps({"word": word}))
p2.sendall(json.dumps({"word": word}))

p1_result = json.loads(p1.recv())
p2_result = json.loads(p2.recv())

p1_score = p1_result["wrong"]
p2_score = p2_result["wrong"]

if p1_score < p2_score:
    winner = "Player 1"
elif p2_score < p1_score:
    winner = "Player 2"
else:
    winner = "Tie"

print("Player 1:", p1_score)
print("Player 2:", p2_score)
print("Winner:", winner)

