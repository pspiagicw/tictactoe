"""
Tic Tac Toe Player
"""

import math
import itertools
import random
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
    no_of_x = 0
    no_of_o = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                no_of_x += 1
            if board[i][j] == O:
                no_of_o += 1
    if no_of_o == no_of_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = list()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i , j = action
    board_result = copy.deepcopy(board)
    board_result[i][j] = player(board)
    return board_result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_winner(board,X):
        return X
    if check_winner(board,O):
        return O
    return None
def check_winner(board,player):
    player_playing = player
    coordinates = list()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player_playing:
                coordinates.append((i,j))
    if len(coordinates) < 3:
        return None
    coordinates_pairs = itertools.permutations(coordinates,3)
    winning_pairs = get_winning_coordinate_pairs()
    for coordinate_trio in coordinates_pairs:
        if list(coordinate_trio) in winning_pairs:
            return player_playing
    return None

def get_winning_coordinate_pairs():
    horizontal_pairs = [ [ (i,j) for j in range(3) ] for i in range(3) ]
    vertical_pairs = [ [ (i,j) for i in range(3) ] for j in range(3) ]
    right_diagonal = [ [ (0,0) , (1,1) , (2 , 2) ]]
    left_diagonal = [ [ (0,2) , (1,1) , (2,0) ] ]
    return horizontal_pairs + vertical_pairs + right_diagonal + left_diagonal

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if  board[i][j] == EMPTY:
                    return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # return random.choice(actions(board))
    if terminal(board):
        return None
    if player(board) == X:
        value , move = max_score(board)
        return move
    if player(board) == O:
        value , move = min_score(board)
        return move
def max_score(board):
    if terminal(board):
        return utility(board) , None
    move = None
    score = -float('inf')
    for  i in actions(board):
        new_score , new_move = min_score(result(board,i))
        if new_score > score:
            score = new_score
            move = i
            if score == 1:
                return score, move
    return score , move
def min_score(board):
    if terminal(board):
        return utility(board),None
    move = None
    score = float('inf')
    for i in actions(board):
        new_score , new_move = max_score(result(board,i))
        if new_score < score:
            score = new_score
            move = i
            if score == -1:
                return score , move
    return score , move
                


