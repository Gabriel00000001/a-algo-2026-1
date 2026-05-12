"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    contador_x = 0
    contador_o = 0
    
    for linha in board:
        for celula in linha:

            if celula == X:
                contador_x += 1
            elif celula == O:
                contador_o += 1

    if contador_x > contador_o:
        return O
    elif contador_x == contador_o:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    movimentos_possiveis = set()

    for i, linha in enumerate(board):
        for j, celula in enumerate(linha):
            if celula == EMPTY:
                movimentos_possiveis.add((i, j))


    return movimentos_possiveis




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    novo_tabuleiro = copy.deepcopy(board)
    jogada_atual = player(board)

    i, j = action
    if board[i][j] is not  EMPTY:
        raise Exception("Jogada Inválida")
    

    novo_tabuleiro[i][j] = jogada_atual

    return novo_tabuleiro






def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    



    for linha in board:
        if linha[0] == linha[1] == linha[2] and linha[0] is not EMPTY:
            return board[0][0]
        
     #coluna 0
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] is not EMPTY:
        return board[0][0]
          
    #coluna 1
    elif board[0][1] == board[1][1] == board[2][1] is not EMPTY:
        return board[0][1]
    
    #coluna 2
    elif board[0][2] == board[1][2] == board[2][2] is not EMPTY:
        return board[0][2]
    
    #diagonal 1
    elif board[0][0] == board[1][1] == board[2][2] is not EMPTY:
        return board[0][0]
    #diagonal 2
    elif board[0][2] == board[1][1] == board[2][0] is not EMPTY:
        return board[0][2]
    
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board)is not None or len(actions(board)) == 0 :
        return True 
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ganhador = winner(board)

    if ganhador == X:
        return 1
    
    elif ganhador == O:
        return -1
    
    else :
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def minimax(board):
        if terminal(board):
            return None

    
    def max_value(s):
        if terminal(s):
            return utility(s)
        v = -float('inf')
        for action in actions(s):
            v = max(v, min_value(result(s, action)))
        return v

    def min_value(s):
        if terminal(s):
            return utility(s)
        v = float('inf')
        for action in actions(s):
            v = min(v, max_value(result(s, action)))
        return v
    # ---------------------------------------------------------

   
    current_player = player(board)
    best_action = None

    if current_player == X:
        max_v = -float('inf')
        for action in actions(board):
            v = min_value(result(board, action))
            if v > max_v:
                max_v = v
                best_action = action
    else:
        min_v = float('inf')
        for action in actions(board):
            v = max_value(result(board, action))
            if v < min_v:
                min_v = v
                best_action = action

    return best_action

