from socket32 import create_new_socket
import json

client = create_new_socket()
client.connect("127.0.0.1", 5555)

while True:
    data = json.loads(client.recv())

    print("\nWord:", " ".join(data["display"]))
    print("Scores:", data["scores"])
    print("You are:", data["your_turn"])

    if "final_word" in data:
        print("\nGame over! Word was:", data["final_word"])
        break

    guess = input("Enter letter: ")
    client.sendall(guess)
