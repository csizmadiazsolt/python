#!/usr/bin/python3

def save_to_file(filename, content):
  open_file = open(filename, 'w')
  open_file.write(content)
  open_file.close()

def get_input(message):
  input_message = str(input(message))
  return input_message
  
filename = get_input("Enter the filename: ")
content = get_input("Enter the content: ")

save_to_file(filename, content)