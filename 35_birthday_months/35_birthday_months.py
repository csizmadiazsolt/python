#!/usr/bin/python3
import json
from collections import Counter

FILE = "birthday_dictionary.json"

def read_dictionary(file_name):
  with open(file_name, "r") as f:
    birthday_dictionary = json.load(f)

  return birthday_dictionary

def number_to_month(number):
  month_switch = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "Decembe",
  }

  return month_switch.get(number, "Invalid month")

def count_months(month_list):
  month_count = Counter(month_list)
  
  return month_count

def get_months_list(dictionary):
  month_list = []
  for key, value in dictionary.items():
    month_list.append(number_to_month(int(value.split(".")[1])))

  return month_list

dictionary = read_dictionary(FILE)
months = get_months_list(dictionary)
month_count = count_months(months)
result = dict(month_count)

print(result)