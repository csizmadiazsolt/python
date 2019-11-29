#!/usr/bin/python3
a = [5, 10, 15, 20, 25]

def first_and_last_element_list(list):
  return [list[0],list[len(list)-1]]

print(first_and_last_element_list(a))