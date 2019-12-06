#!/usr/bin/python3
from random import randint

NUM_OF_LINES = 267751

def get_word_from_line_in_file(file_name, line_number):
  counter = 0

  with open(file_name, 'r') as open_file:
    line = open_file.readline()

    while (line and counter < line_number):
      line = open_file.readline()
      counter += 1

  return line

def random_line_number():
  return randint(0, NUM_OF_LINES-1)

def is_the_guess_correct(guess_word, already_guessed, new_guess):
  if new_guess in already_guessed:
    return -1
  elif new_guess not in guess_word:
    return 0
  else:
    return 1

def add_to_already_guessed(already_guessed, new_guess):
  already_guessed_list = already_guessed.append(new_guess)

  return already_guessed_list

def correct_dash_mixture(guess_word, already_guessed):
  mixture = ""
  for l in guess_word:
    if l in already_guessed:
      mixture += l + " "
    else:
      mixture += "_ "

  return mixture

def guess_input_handler():
  guess = input("Guess your letter: ")

  return guess.upper()

def guess_result_handler(guess_result, already_guessed, guess, word, guess_counter):
  counter = guess_counter

  if guess_result == 1:
    add_to_already_guessed(already_guessed, guess)
    print(correct_dash_mixture(word, already_guessed))
  elif guess_result == 0:
    print("Incorrect!")
    counter += 1
  elif guess_result == -1:
    print("Already guessed!")

  return counter

def game_loop():
  guess_counter = 0
  already_guessed = []
  random_line = random_line_number()
  random_word = get_word_from_line_in_file("sowpods.txt", random_line)
  dash_letter_mixture = correct_dash_mixture(random_word, already_guessed)

  print("Welcome to Hangman!")
  print(dash_letter_mixture)

  while True:
    guess = guess_input_handler()
    guess_result = is_the_guess_correct(random_word, already_guessed, guess)
    guess_counter = guess_result_handler(guess_result, already_guessed, guess, random_word, guess_counter)

game_loop()