from socket32 import create_new_socket
import json
import random
import requests

# ----------------------------
# WORD SOURCE (Wikipedia)
# ----------------------------
def get_wiki_word():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    headers = {"User-Agent": "HangmanProject/1.0 (student project)"}

    data = requests.get(url, headers=headers).json()
    return data["title"].lower()


# ----------------------------
# SERVER SETUP
# ----------------------------
server = create_new_socket()
server.bind("127.0.0.1", 5555)
server.listen()

print("Waiting for players...")

p1, addr1 = server.accept()
print("Player 1 connected:", addr1)

p2, addr2 = server.accept()
print("Player 2 connected:", addr2)


# ----------------------------
# PICK WORD
# ----------------------------
word = get_wiki_word()
print("WORD (debug only):", word)


# ----------------------------
# SEND WORD TO BOTH PLAYERS
# ----------------------------
payload = json.dumps({"word": word})

p1.sendall(payload)
p2.sendall(payload)


# ----------------------------
# WAIT FOR RESULTS SAFELY
# ----------------------------
print("Waiting for results from players...")

p1_data = p1.recv()
p2_data = p2.recv()

# Safety checks (prevents JSON crash)
if not p1_data or not p2_data:
    print("A player disconnected or sent no data.")
    p1.close()
    p2.close()
    server.close()
    exit()

try:
    p1_result = json.loads(p1_data)
    p2_result = json.loads(p2_data)
except json.JSONDecodeError:
    print("Invalid JSON received from a client.")
    p1.close()
    p2.close()
    server.close()
    exit()


# ----------------------------
# EXTRACT SCORES
# ----------------------------
p1_wrong = p1_result.get("wrong", 999)
p2_wrong = p2_result.get("wrong", 999)


# ----------------------------
# DETERMINE WINNER
# ----------------------------
print("\n--- RESULTS ---")
print("Player 1 wrong guesses:", p1_wrong)
print("Player 2 wrong guesses:", p2_wrong)

if p1_wrong < p2_wrong:
    winner = "Player 1"
elif p2_wrong < p1_wrong:
    winner = "Player 2"
else:
    winner = "Tie"

print("Winner:", winner)


# ----------------------------
# SEND FINAL RESULT TO CLIENTS
# ----------------------------
final_msg = json.dumps({
    "word": word,
    "p1_wrong": p1_wrong,
    "p2_wrong": p2_wrong,
    "winner": winner
})

p1.sendall(final_msg)
p2.sendall(final_msg)


# ----------------------------
# CLEANUP
# ----------------------------
p1.close()
p2.close()
server.close()
