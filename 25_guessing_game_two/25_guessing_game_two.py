#!/usr/bin/python3
top = 100
bottom = 0
counter = 0

print("Enter \"l\" if your guess is lower, enter \"h\" if your guess is higher. And enter \"c\" is the guess if correct!\n")

while True:
  guess = int((top + bottom) / 2)
  low_high = input("Is your guess {}? [l/h/c]: ".format(guess))
  counter += 1
  
  if low_high == "l":
    top = guess
  elif low_high == "h":
    bottom = guess
  elif low_high == "c":
    break

print("Number of guesses: {}".format(counter))