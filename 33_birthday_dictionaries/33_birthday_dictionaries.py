#!/usr/bin/python3

MSG_WELCOME = "Welcome to the birthday dictionary. We know the birthdays of:"
MSG_WHOSBDAY = "\nWho's birthday do you want to look up?\n"

def read_dictionary(file_name):
  birthday_dictionary = {}

  with open(file_name, 'r') as open_file:
    line = remove_line_end(open_file.readline())
    while line:
      name_and_date = get_name_and_date(line)
      name = str(name_and_date[0])
      date = str(name_and_date[1])

      birthday_dictionary[name] = date

      line = remove_line_end(open_file.readline())

  return birthday_dictionary

def print_names(dictionary):
  for name in dictionary.keys():
    print(" - " + str(name))

def get_date(name, dictionary):
  return dictionary[name]

def get_name_and_date(line):
  return line.split(",")

def remove_line_end(line):
  if "\n" in line:
    line = line[:len(line)-1]

  return line

def query_handler():
  print(MSG_WELCOME)

  dictionary = read_dictionary("birthday_dictionary.txt")
  print_names(dictionary)

  name = input(MSG_WHOSBDAY)
  date = get_date(name, dictionary)

  print("\n" + name + "'s birthday is " + str(date) + ".")
  
query_handler()