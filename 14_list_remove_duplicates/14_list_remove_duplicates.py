#!/usr/bin/python3

def no_duplicates_in_list_impl1(input_list):
  return list(set(input_list))

def no_duplicates_in_list_impl2(input_list):
  new_list = []

  for i in input_list:
    if i not in new_list:
      new_list.append(i)

  return new_list

tester = ['A', 'B', 'C', 'D', 'X', 'A']

print(no_duplicates_in_list_impl1(tester))
print(no_duplicates_in_list_impl2(tester))