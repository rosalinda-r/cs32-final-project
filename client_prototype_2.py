from socket32 import create_new_socket
import json

client = create_new_socket()
client.connect("127.0.0.1", 5555)

data = json.loads(client.recv())
word = data["word"]
