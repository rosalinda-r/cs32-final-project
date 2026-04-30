import socket
import json

HOST = "localhost"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    data = client.recv(4096).decode()
    state = json.loads(data)

    print("\nWord:", " ".join(state["display"]))
    print("Scores:", state["score"])
    print("Your turn:", state["your_turn"])

    if "final_word" in state:
        print("\nGame Over!")
        print("Word was:", state["final_word"])
        break

    guess = input("Enter letter: ")
    client.send(guess.encode())
