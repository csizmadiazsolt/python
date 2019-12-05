#!/usr/bin/python3

VERT_SEGMENT = " ---"
HORI_SEGMENT1 = "| "
HORI_SEGMENT2 = " "
HORI_END_SEGMENT = "|"

EMPTY = " "
PLAYER1 = "O"
PLAYER2 = "X"

def draw_board(size_x, size_y, game_matrix):
  for i in range(0,size_y):
    for _ in range(0,size_x):
      print(VERT_SEGMENT,end="")
    print("\n",end="")
    for k in range(0,size_x):
      print(HORI_SEGMENT1,end="")
	  
      if game_matrix[i][k] == 0:
        print(EMPTY,end="")
      elif game_matrix[i][k] == 1:
        print(PLAYER1,end="")
      elif game_matrix[i][k] == 2:
        print(PLAYER2,end="")

      print(HORI_SEGMENT2,end="")
    print(HORI_END_SEGMENT)
  for _ in range(0,size_x):
    print(VERT_SEGMENT,end="")

game = [[1, 0, 2],
	    [0, 1, 0],
	    [0, 0, 2]]

draw_board(3, 3, game)