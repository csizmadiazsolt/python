#!/usr/bin/python3
import json

MSG_WELCOME = "Welcome to the birthday dictionary. We know the birthdays of:"
MSG_WHOSBDAY = "\nWho's birthday do you want to look up?\n"
MSG_NO_RES = "\nNo such name in the dictionary!"
MSG_RES = "\n{}'s birthday is {}."
MSG_SAVE = "New name and birthday saved!"

FILE = "birthday_dictionary.json"

def read_dictionary(file_name):
  with open(file_name, "r") as f:
    birthday_dictionary = json.load(f)

  return birthday_dictionary

def print_names(dictionary):
  for name in dictionary.keys():
    print(" - " + str(name))

def get_date(name, dictionary):
  try:
    return dictionary[name]
  except KeyError:
    print(MSG_NO_RES)

def new_user():
  while True:
    new_user_yn = input("\nWould you like to add a new name and birthday? [y/n]: ")

    if new_user_yn == "y":
      name = input("Name: ")
      birthday = input("Birthday: ")
      return [name, birthday]
    elif new_user_yn == "n":
      break

def add_element_to_dictionary(dictionary, name, birthday):
  updated_dictionary = dictionary
  
  updated_dictionary[name] = birthday
  return updated_dictionary

def save_dictionary_to_file(file_name, dictionary):
  with open(file_name, "w") as f:
    json.dump(dictionary, f)

  print(MSG_SAVE)

def save_new_user(dictionary):
  new_user_name_and_birthday = new_user()

  if new_user_name_and_birthday:
    new_name = new_user_name_and_birthday[0]
    new_birthday = new_user_name_and_birthday[1]
    dictionary = add_element_to_dictionary(dictionary, new_name, new_birthday)
    save_dictionary_to_file(FILE, dictionary)

def query_handler(dictionary):
  print(MSG_WELCOME)

  print_names(dictionary)

  name = input(MSG_WHOSBDAY)
  date = get_date(name, dictionary)

  if date:
    print(MSG_RES.format(name, date))

dictionary = read_dictionary(FILE)
query_handler(dictionary)
save_new_user(dictionary)