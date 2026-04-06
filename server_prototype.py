import random
from socket32 import create_new_socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    with create_new_socket() as s:
        # Bind socket to address and publish contact info
        s.bind(HOST, PORT)
        s.listen()
        print("HANGMAN! server started. Listening on", (HOST, PORT))
        words = ['cosmo', 'wanda', 'waldo', 'odlaw', 'cat', 'hat', 'tuple', 'roshambo', 'list', 'coarsen']

        # Answer incoming connection
        conn2client, addr = s.accept()
        print('Connected by', addr)

        with conn2client:
            while True:   # message processing loop
                choice = conn2client.recv()
                if choice == '':
                    break
                choice = str(shape)

                # Generate a random shape to send back to client
                # Create a secret for this connection
                option = random.choice(words)
                conn2client.sendall(option)



            print('Disconnected')

if __name__ == '__main__':
    main()
