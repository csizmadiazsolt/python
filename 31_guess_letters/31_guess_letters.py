#!/usr/bin/python3

WORD = "EVAPORATE"

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

def guess_result_handler(guess_result, already_guessed, guess):
  if guess_result == 1:
    add_to_already_guessed(already_guessed, guess)
    print(correct_dash_mixture(WORD, already_guessed))
  elif guess_result == 0:
    print("Incorrect!")
  elif guess_result == -1:
    print("Already guessed!")

def game_loop():
  already_guessed = []
  dash_letter_mixture = correct_dash_mixture(WORD, already_guessed)

  print("Welcome to Hangman!")
  print(dash_letter_mixture)

  while True:
    guess = guess_input_handler()
    guess_result = is_the_guess_correct(WORD, already_guessed, guess)
    guess_result_handler(guess_result, already_guessed, guess)

game_loop()