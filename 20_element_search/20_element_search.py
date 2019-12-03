#!/usr/bin/python3
import math
import timeit

def is_in_list_impl1(ordered_list, number):
  if number in ordered_list:
    return True
  else:
    return False

def binary_search(A_list, T_target):
  L = 0
  R = len(A_list)-1

  while L <= R:
    m = math.floor((L+R)/2)

    if A_list[m] < T_target:
      L = m+1
    elif A_list[m] > T_target:
      R = m-1
    else:
      return True

  return False

elements = [4,6,9,11,35,48,56,111,368,421]
num_1 = 11
num_2 = 12

print("Built-in solution:")
print("------------------")
print("Is " + str(num_1) + " in " + str(elements) + "? --> ", end="")
print(is_in_list_impl1(elements,num_1))
print("Is " + str(num_2) + " in " + str(elements) + "? --> ", end="")
print(is_in_list_impl1(elements,num_2))

print("\nBinary search solution:")
print("-----------------------")
print("Is " + str(num_1) + " in " + str(elements) + "? --> ", end="")
print(binary_search(elements,num_1))
print("Is " + str(num_2) + " in " + str(elements) + "? --> ", end="")
print(binary_search(elements,num_2))