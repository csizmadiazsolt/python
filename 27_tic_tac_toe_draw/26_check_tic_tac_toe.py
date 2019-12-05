#!/usr/bin/python3

def line_match(game_status):
  for i in range(3):
    if(game_status[i][0] == game_status[i][1] == game_status[i][2]):
      return game_status[i][0]
    if(game_status[0][i] == game_status[1][i] == game_status[2][i]):
      return game_status[0][i]

  return 0

def diagonal_match(game_status):
  if((game_status[0][0] == game_status[1][1] == game_status[2][2])
  or (game_status[0][2] == game_status[1][1] == game_status[2][0])):
    return game_status[1][1]

  return 0

def who_won(game_status):
  line_match_res = line_match(game_status)
  diagonal_match_res = diagonal_match(game_status)

  if line_match_res > 0:
    return line_match_res
  elif diagonal_match_res > 0:
    return diagonal_match_res
  else:
    return 0

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

print(who_won(winner_is_2))
print(who_won(winner_is_1))
print(who_won(winner_is_also_1))
print(who_won(no_winner))
print(who_won(also_no_winner))