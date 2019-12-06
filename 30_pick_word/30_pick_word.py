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

random_word = get_word_from_line_in_file("sowpods.txt", random_line_number())
print(random_word)