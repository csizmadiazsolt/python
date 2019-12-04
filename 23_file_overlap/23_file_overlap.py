#!/usr/bin/python3

def read_file_to_list(file_name):
  number_list = []
  
  with open(file_name, 'r') as open_file:
    line = remove_line_end(open_file.readline())
    while line:
      number_list.append(line)
      line = remove_line_end(open_file.readline())

  return number_list

def remove_line_end(line):
  if "\n" in line:
    line = line[:len(line)-1]

  return line

def overlap_list(list_a, list_b):
  overlap_list = []
  
  for element in list_a:
    if element in list_b:
      overlap_list.append(element)

  return overlap_list

list_1 = read_file_to_list("primenumbers.txt")
list_2 = read_file_to_list("happynumbers.txt")
list_3_overlap = overlap_list(list_1, list_2)

print(list_3_overlap)