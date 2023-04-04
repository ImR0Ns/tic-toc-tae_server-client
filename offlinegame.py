import tic_tac_toe

if __name__ == "__main__":

    print("Player 1")
    p1name = input("Enter the name : ")
    print("\n")

    player1 = tic_tac_toe.Player(p1name, "X")

    print("Player 2")
    p2name = input("Enter the name : ")
    print("\n")

    player2 = tic_tac_toe.Player(p2name, "O")

    cur_player = player1

    board = tic_tac_toe.init_board()
    winner = None
    crt_player = player1
    while True:
        table = tic_tac_toe.print_tic_tac_toe(board)
        print(table)
        if tic_tac_toe.check_draw(board):
            break
        if tic_tac_toe.check_win(crt_player):
            winner = crt_player
            break

        move = input("Enter move: ")
        new_board = tic_tac_toe.play_move(crt_player, board, move)
        if not new_board:
            print("Invalid move. Try again!")
            continue
        board = new_board

        if crt_player is player1:
            crt_player = player2
        else:
            crt_player = player1

    if winner:
        print(f"Player {player1.name} won")
    else:
        print("Game finished in a draw!")
