import sys, socket
import echo_util

HOST = '127.0.0.1'
PORT = echo_util.PORT

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))  #connect to server
        print("here")
    except ConnectionError:
        print('Socket error on connection')
        sys.exit(1)

    print('\nConnected to {}:{}'.format(HOST, PORT))
    print("Type message, enter to send, 'q' to quit")
    print("Please enter your name:")

    while True:
        msg = input()
        if not msg:
            continue

        if msg == 'q': break
        try:
            echo_util.send_msg(sock, msg) # Blocks until sent
            print('Sent message: {}'.format(msg))
            msg = echo_util.recv_msg(sock)
            # Block until
            # received complete
            # message
            print('Received echo: ' + msg)
            print(echo_util.recv_msg(sock))
        except ConnectionError:
            print('Socket error during communication')
            sock.close()
            print('Closed connection to server\n')
            break

    print("Closing connection")
    sock.close()
