#!/usr/bin/python3
import time

current_year = time.localtime().tm_year

name = input("What's your name: ")
age = int(input("What's your age: "))

result = str(current_year + 100 - age)

print("\n" + name + " will be 100 years old in " + result + "\n");

for num in range(age,101):
  result = str(current_year + num - age)
  print(name + " will be " + str(num) + " years old in " + result);