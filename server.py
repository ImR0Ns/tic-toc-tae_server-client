import echo_util
import threading
import tic_tac_toe

HOST = '127.0.0.1'
PORT = echo_util.PORT

cons = [] #conexiuni
players = [] #jucatori init prin modelul dat


def handle_client(sock, addr):
    """ Receive data from the client via sock and echo it back """

    player = False # initializare player


    while not player:
        player_name = echo_util.recv_msg(sock) 
        if len(cons) == 1:
            player = tic_tac_toe.Player(player_name, "X") # primul
        else: #al doilea cu check-uri
            if players[0].name == player_name:
                echo_util.send_msg(sock, "Numele a fost luat!")
                continue
            else:
                player = tic_tac_toe.Player(player_name, "0")
    
    if player:
        players.append(player)

    if len(players) == 2:
        board = tic_tac_toe.init_board() #cand ajunge la doi jucatori conectati dam start la joc
    else:
        board = False

    i = 0 # jucator current idx la socket 
    while True and board != False:
        try:
            table = tic_tac_toe.print_tic_tac_toe(board)
            echo_util.send_msg(cons[i], table) # aratam tabla
            
            echo_util.send_msg(cons[i], "Miscarea ta: ")
            move = echo_util.recv_msg(cons[i])

            new_board = tic_tac_toe.play_move(players[i], board, move, cons, i)
            if not new_board:
                echo_util.send_msg(cons[i], "Miscare necorespunzatoare!")
                continue
            board = new_board

            if tic_tac_toe.check_draw(board):
                for con in cons:
                    echo_util.send_msg(con, "Egal!")
                    echo_util.send_msg(con, "Jocul s-a terminat!") #jocul este gata
                break
            
            if tic_tac_toe.check_win(players[i]):
                for con in cons:
                    echo_util.send_msg(con, f"Jucatorul {players[i].name} a castigat!") #castigator display
                    echo_util.send_msg(con, "Jocul s-a terminat!") #jocul este gata
                break 

            if i == 0:
                i = 1
            else:
                i = 0

        except (ConnectionError, BrokenPipeError):
            print('Closed connection to {}'.format(addr))
            sock.close()
            break

if __name__ == '__main__':
    listen_sock = echo_util.create_listen_socket(HOST, PORT)
    addr = listen_sock.getsockname()
    print('Listening on {}'.format(addr))

    while True:
        if len(cons) < 2 :
            client_sock, addr = listen_sock.accept()
            # Thread will run function handle_client() autonomously
            # and concurrently to this while loop
            thread = threading.Thread(target = handle_client, args = [client_sock, addr], daemon=True)
            thread.start()
            cons.append(client_sock)
            print('Connection from {}'.format(addr))
