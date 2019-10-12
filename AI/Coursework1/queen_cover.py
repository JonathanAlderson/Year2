## Definition of Queens search problem
## For use with queue_search.py
from __future__ import print_function
from copy import deepcopy
import time

def queen_get_initial_state(x,y):
      return ( 0, 0, matrix_of_zeros(y,x) )

def matrix_of_zeros(X,Y):
    return [ [0 for x in range(X)] for y in range(Y)] # Pythonic or what? ikr


def queen_possible_actions( state ):
             # returns every move a queen could make
             if state[0] == 0:
                return queen_initial_moves()
             return queen_following_moves(state)

def queen_initial_moves():
           # since the queen can start at any position
           moves = []
           for i in range(BOARD_X):
               for j in range(BOARD_Y):
                   moves = moves + [[i,j]]
           return moves

def square_is_empty(i,j, state):
      if state[2][i][j] == 0:
         return True
      return False

# since this is not the knights tour, we can simply
# move the queen in any direction, keeping it between 2 and 2
# gives the best results
queens_moves = tuple([(i,j) for j in range(2) for i in range(2)])

def queen_following_moves( state ):
      kx = state[1][0]
      ky = state[1][1]
      moves = []
      for move in queens_moves:
           newx = kx + move[0]    ## target x coord
           newy = ky + move[1]    ## target y coord

           ## If target square is on board and empty
           ## add it to the list of moves
           if newx in range(BOARD_X) and newy in range(BOARD_Y):
              if state[2][newx][newy] == 0:
                 moves = moves + [move]
      return moves

def queen_successor_state( action, state ):
    if state[0] == 0:
       newstate =  queen_initial_successor( action )
       return newstate
    board = deepcopy(state[2])
    xpos = state[1][0] + action[0]
    ypos = state[1][1] + action[1]
    movenum = state[0] + 1
    board[xpos][ypos] = movenum
    return (movenum, (xpos,ypos), board)


def queen_initial_successor( action ):
    board = deepcopy(queen_initial_state[2])
    board[action[0]][action[1]] = 1
    return( 1, action, board )


def queen_goal_state( state ):
       if check_free_squares(state):
          print( "\nGOAL STATE:" )
          print_board_state( state ) # prints out the board
                                     # as well so we can see
          return True
       return False

def check_free_squares( state ):

    # function returns the number of spaces which are
    #    not controlled by a queen

    # we first make list of rows and columns that are occupied by queens
    takenRows = []
    takenCols = []

    # since on a diagonal the sum of i + j is the same,
    # we can just keep a list of the sum of i+j, if any square has
    # the same sum as anything on the forward diags list, then the space
    # has been threatened by a queen.

    # for reverse diags we use ( BOARD_X - i ) + j and this gives all the
    # diagons but in the other direction

    forwardDiags = []
    reverseDiags = []

    for i in range(BOARD_X):
        # checks to see if there is a non-zero item anywhere in the row (queen)
        if(not (all(v == 0 for v in state[2][i]))):
            takenRows.append(i)
            for j in range(BOARD_Y):
                if(state[2][i][j] != 0):
                    # add the column
                    if(j not in takenCols):
                        takenCols.append(j)
                    # add the diagonal
                    if(i+j not in forwardDiags):
                        forwardDiags.append(i+j)
                    # add the reverse diagonal
                    if((BOARD_X - i)+j not in reverseDiags):
                        reverseDiags.append((BOARD_X -i)+j)

    # now we have lists of every row which has a queen on
    # every column which has a queen on
    # and every diagonal that has a queen on
    for i in range(BOARD_X):
        for j in range(BOARD_Y):
            # only one if statement has to be false for the space to be taken
            # for the sake of efficiency we check the rows first, then the cols.
            if(i not in takenRows):
                if(j not in takenCols):
                    if(i+j not in forwardDiags):
                        if((BOARD_X-i)+j not in reverseDiags):
                            # there is a free space not controlled by a queen.
                            # so return false
                            return False
    # the board is fully covered by queens
    return True


def print_board_state( state ):
      # same as before but with nicer formatting
      board = state[2]
      print("\n ",end='')
      for i in range(len(board[0])):
          print("  " + str(i+1),end = '')
      print("\n")
      for i in range(len(board)):
           print(str(i+1),end = '')
           for square in board[i]:
               print( " %2i" % square, end = '' )
           print()
      print("\n")





def queen_print_problem_info():
    print( "The Queens Problem (", BOARD_X, "x", BOARD_Y, "board)" )

## Return a problem spec tuple for a given board size
def make_qc_problem(x, y):
      global BOARD_X, BOARD_Y, queen_initial_state
      BOARD_X = x
      BOARD_Y = y
      queen_initial_state = queen_get_initial_state(x,y)
      return  ( None,
                queen_print_problem_info,
                queen_initial_state,
                queen_possible_actions,
                queen_successor_state,
                queen_goal_state
              )
