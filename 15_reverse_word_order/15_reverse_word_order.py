#!/usr/bin/python3

def reverse(input):
  splitted = input.split(" ")
  splitted.reverse()
  
  return " ".join(splitted)

def input_handler():
  while True:
    sentence = str(input("Enter a sentence: "))
    if sentence.find(" ") > 0:
      break
    else:
      print("There is no space in your input. ", end="")

  return sentence
	
input = input_handler()
print(reverse(input))