#!/usr/bin/python3

VERT_SEGMENT = " ---"
HORI_SEGMENT1 = "| "
HORI_SEGMENT2 = " "
HORI_END_SEGMENT = "|"

EMPTY = " "
PLAYER1 = "O"
PLAYER2 = "X"

MAX_X = 3
MAX_Y = 3

ERROR_MSG_NO_COMMA = "ERROR: There is no , in the input!"
ERROR_MSG_ONLY_XY = "ERROR: Only X and Y coordinates are needed!"
ERROR_MSG_NUMERIC = "ERROR: Inputs should be numeric!"
ERROR_MSG_X_BETWEEN = "ERROR: X should be between 1 and "
ERROR_MSG_Y_BETWEEN = "ERROR: Y should be between 1 and "
ERROR_MSG_COLLISION = "Collision!!!"

WIN_MSG_NO_WINNER = "\nThere is no winner..."
WIN_MSG_PLAYER1 = "\nThe winner is PLAYER1: "
WIN_MSG_PLAYER2 = "\nThe winner is PLAYER2: "

INPUT_MSG = " - [x,y]: "

def draw_board(size_x, size_y, game_matrix):
  for i in range(0,size_y):
    for _ in range(0,size_x):
      print(VERT_SEGMENT,end="")
    print("\n",end="")
    for k in range(0,size_x):
      print(HORI_SEGMENT1,end="")
	  
      if game_matrix[k][i] == 0:
        print(EMPTY,end="")
      elif game_matrix[k][i] == 1:
        print(PLAYER1,end="")
      elif game_matrix[k][i] == 2:
        print(PLAYER2,end="")

      print(HORI_SEGMENT2,end="")
    print(HORI_END_SEGMENT)
  for _ in range(0,size_x):
    print(VERT_SEGMENT,end="")

def line_match(game_matrix):
  for i in range(3):
    if(game_matrix[i][0] == game_matrix[i][1] == game_matrix[i][2]):
      return game_matrix[i][0]
    if(game_matrix[0][i] == game_matrix[1][i] == game_matrix[2][i]):
      return game_matrix[0][i]

  return 0

def diagonal_match(game_matrix):
  if((game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2])
  or (game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0])):
    return game_matrix[1][1]

  return 0

def end_of_game_without_winner(game_matrix):
  num_of_engaged = 0

  for i in range(0,3):
    for j in range(0,3):
      if game_matrix[i][j] > 0:
        num_of_engaged += 1

  if num_of_engaged == 9:
    return True
  else:
    return False

def who_won(game_matrix):
  line_match_res = line_match(game_matrix)
  diagonal_match_res = diagonal_match(game_matrix)
  end_of_game = end_of_game_without_winner(game_matrix)

  if line_match_res > 0:
    return line_match_res
  elif diagonal_match_res > 0:
    return diagonal_match_res
  elif end_of_game == True:
    return -1
  else:
    return 0
	
def winner_info(status):
  if status == -1:
    print(WIN_MSG_NO_WINNER)
  elif status == 1:
    print(WIN_MSG_PLAYER1 + PLAYER1)
  elif status == 2:
    print(WIN_MSG_PLAYER2 + PLAYER2)

def input_checker(input_string, range_x, range_y):
  error_flag = True
  is_numeric_flag = True

  if "," not in input_string:
    print(ERROR_MSG_NO_COMMA)
    error_flag = False

  splitted_input = input_string.split(",")
  
  if len(splitted_input) > 2:
    print(ERROR_MSG_ONLY_XY)
    error_flag = False

  if ((splitted_input[0].isnumeric() == False)
  or (splitted_input[1].isnumeric() == False)):
    print(ERROR_MSG_NUMERIC)
    is_numeric_flag = False
    error_flag = False
	
  if ((is_numeric_flag == False)
  or (range_x < int(splitted_input[0]))
  or (int(splitted_input[0]) < 1)):
    print(ERROR_MSG_X_BETWEEN + str(range_x))
    error_flag = False

  if ((is_numeric_flag == False)
  or (range_y < int(splitted_input[1]))
  or (int(splitted_input[1]) < 1)):
    print(ERROR_MSG_Y_BETWEEN + str(range_y))
    error_flag = False

  if error_flag == False:
    return False
  else:
    return splitted_input

def collision_detection(game_matrix, x, y):
  if game_matrix[x][y] > 0:
    return True

  return False

def input_handler(game_matrix, player):
  message = ""

  if player == 1:
    message = "\n" + PLAYER1 + INPUT_MSG
  elif player == 2:
    message = "\n" + PLAYER2 + INPUT_MSG

  value = str(input(message))
  result = input_checker(value, MAX_X, MAX_Y)
  
  if result != False:
    x = int(result[0])
    y = int(result[1])
    collision = collision_detection(game_matrix, x-1, y-1)
  
    if collision == True:
      print(ERROR_MSG_COLLISION)
      return False	

    numeric_result = [x, y]
    return numeric_result

  return False

def update_game(game, player, x, y):
  new_game = game
  new_game[x-1][y-1] = player
  
  return new_game

def whos_turn(current):
  if current == 1:
    return 2
  return 1

def game_loop():
  current_player = 1
  game = [[0, 0, 0],
	      [0, 0, 0],
	      [0, 0, 0]]

  draw_board(3, 3, game)

  while True:
    x_y_input = input_handler(game, current_player)

    if x_y_input != False:
      game = update_game(game, current_player, x_y_input[0], x_y_input[1])
      draw_board(3, 3, game)
      winner = who_won(game)
	  
      if winner != 0:
        winner_info(winner)
        break
	  
      current_player = whos_turn(current_player)

game_loop()