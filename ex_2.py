#!/usr/bin/python3

number = int(input("Enter a number: "))

if (number % 2 == 0):
  if (number % 4 == 0):
    print("This number is even and multiple of 4!")
  else:
    print("This number is even!")
else:
  print("This number is odd!")