#!/usr/bin/python3
from random import randint

def generate_password(length):
  password = ""

  for _ in range(0,length):
    pass_char = randint(33,126)
    password += chr(pass_char)
	
  return password

print(generate_password(15))