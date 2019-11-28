#!/usr/bin/python3
from random import randint

generated_number = randint(1,9)
number_of_attempts = 0

print("Use 'exit' if you want to exit the application!\n")

while True:
  user_command = input("Guess a number between 1-9: ")
  number_of_attempts += 1
  
  if(user_command.isnumeric()):
    if(int(user_command) > generated_number):
      print("Too high!")
    elif(int(user_command) < generated_number):
      print("Too low!")
    elif(int(user_command) == generated_number):
      print("Exactly right!")
      break
  else:
    if(user_command == "exit"):
      break
    else:
      continue
	  
print("\nNumber of attempts: " + str(number_of_attempts))