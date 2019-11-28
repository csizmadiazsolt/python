#!/usr/bin/python3
from random import randint

def user_input():
  player_1_name = str(input("Player 1: "))
  player_2_name = str(input("Player 2: "))
  
  players = [player_1_name,player_2_name]
  
  return players

def num_to_value(num):
  if(num == 0):
    return "rock"
  elif(num == 1):
    return "paper"
  else:
    return "scissors"

def game(players):
  player_1_result = randint(0,2)
  player_2_result = randint(0,2)

  while player_1_result == player_2_result:
    player_1_result = randint(0,2)
    player_2_result = randint(0,2)
  
  #0=rock, 1=paper, 2=scissors
  if((player_1_result == 0 and player_2_result == 2)
    or (player_1_result == 2 and player_2_result == 1)
	or (player_1_result == 1 and player_2_result == 0)):
      print("\nThe winner is " + players[0] + " (" + str(num_to_value(player_1_result)) + " beats " + str(num_to_value(player_2_result)) + ")")
  else:
    print("\nThe winner is " + players[1] + " (" + str(num_to_value(player_1_result)) + " beats " + str(num_to_value(player_2_result)) + ")")

def game_loop():
  players = user_input()
  game(players)
  
  while True:
    user_command = str(input("Would you like to play again [y/n]: "))

    if user_command == "y":
      game(players)
    elif user_command == "n":
      break
    else:
      continue

game_loop()