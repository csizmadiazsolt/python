#!/usr/bin/python3

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

compare = int(input("Enter a number: "))

for index in range(len(list)):
  if list[index] < compare : new_list.append(list[index])

print(*new_list, sep=', ')