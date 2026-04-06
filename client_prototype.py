from socket32 import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def main():
    print('## Welcome to ROSHAMBO! ##')

    with create_new_socket() as s:
        s.connect(HOST, PORT)


            # Grab a guess from the player
        while True:
            shape = str(input('Please pick your shape: '))
            if shape in ['rock', 'paper', 'scissors']:
                break
            else:
                print('Shape must be rock, paper, or scissors. Try again...')

        s.sendall(shape)
        computer = s.recv()
        print(f"You: {shape}   Computer: {computer}")

        if shape == computer:
            print("It's a tie!")

        elif shape == 'rock':
            if computer == 'scissors':
                print('You win!')

            else:
                print('You lose!')

        elif shape == 'paper':
            if computer == 'rock':
                print('You win!')

            else:
                print('You lose!')

        elif shape == 'scissors':
            if computer == 'paper':
                print('You win!')

            else:
                print('You lose!')


if __name__ == '__main__':
    main()
