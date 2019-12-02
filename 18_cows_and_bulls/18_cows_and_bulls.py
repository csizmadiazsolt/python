#!/usr/bin/python3
from random import randint

def random_four_digit_number():
  return randint(1000,9999)

def number_of_cows(number, guess):
  cow_counter = 0

  for i in range(0,4):
    if number[i] == guess[i]:
      cow_counter += 1

  return cow_counter

def number_of_bulls(number, guess, cows):
  bull_counter = 0

  for i in guess:
    if i in number:
      bull_counter += 1

  return bull_counter - cows	

def game_loop():
  number_of_attempts = 0
  random_number = str(random_four_digit_number())
  
  while True:
    your_guess = str(input("Enter a number: "))
    number_of_attempts += 1
    cows = number_of_cows(random_number, your_guess)
    bulls = number_of_bulls(random_number, your_guess, cows)

    if cows == 4:
      break

    print(str(cows) + " cows, " + str(bulls) + " bulls")
	
  print("Congratulation, you win! Number of attempts: " + str(number_of_attempts))

game_loop()