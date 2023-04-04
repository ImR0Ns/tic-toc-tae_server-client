import echo_util

class Player:
    def __init__(self, name, simbol):
        self.name = name
        self.simbol = simbol
        self.moves_made = []


# Convenience function to print game board
def print_tic_tac_toe(values):
    msg = ''
    msg += "\n"
    msg += "\t     |     |\n"
    msg += "\t  {}  |  {}  |  {}\n".format(values[0], values[1], values[2])
    msg += "\t_____|_____|_____\n"

    msg += "\t     |     |\n"
    msg += "\t  {}  |  {}  |  {}\n".format(values[3], values[4], values[5])
    msg += "\t_____|_____|_____\n"

    msg += "\t     |     |\n"

    msg += "\t  {}  |  {}  |  {}\n".format(values[6], values[7], values[8])
    msg += "\t     |     |\n"
    msg += "\n"

    return msg


# Verifica daca vreuna din mutarile jucatorului sunt castigatoare
def check_win(player: Player):
    winning_pos = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]

    for x in winning_pos:
        if all(y in player.moves_made for y in x):
            return True

    return False


# Verificare naiva de egalitate
def check_draw(board):
    if board.count(" ") == 0:
        return True

    return False


def init_board():
    board = [" " for _ in range(9)]
    return board


def play_move(player: Player, board, move, cons, i):
    try:
        move = int(move)
    except ValueError:
        #print("Mutare non-int")
        echo_util.send_msg(cons[i], "Mutare non-int")
        ## Atentioneza clientul ca nu a furnizat o valoare corecta
        return None

    if move < 1 or move > 9:
        #print("Mutare ilegala")
        echo_util.send_msg(cons[i], "Mutare ilegala")
        ## Atentioneaza clientul ca nu a furnizat o valoare corecta
        return None

    if board[move - 1] != " ":
        #print("Mutare pe patrat ocupat")
        echo_util.send_msg(cons[i], "Mutare pe patrat ocupat")
        ## Atentioneaza clientul ca nu a furnizat o valoare corecta
        return None

    board[move - 1] = player.simbol
    player.moves_made.append(move)
    return board
