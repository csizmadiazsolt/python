#!/usr/bin/python3

def file_reader(file_name):
  dictionary = {}
  
  with open(file_name, 'r') as open_file:
    line = remove_line_end(open_file.readline())
    while line:
      if is_key_in_dictionary(dictionary, line) == True:
        dictionary[line] += 1
      else:
        dictionary[line] = 1
      line = remove_line_end(open_file.readline())

  return dictionary

def is_key_in_dictionary(dictionary, key_to_check):
  keys = dictionary.keys()

  if key_to_check in keys:
    return True

  return False

def remove_line_end(line):
  if "\n" in line:
    line = line[:len(line)-1]

  return line

print(file_reader("nameslist.txt"))