#!/usr/bin/python3

def max_of_three(a, b, c):
  max = 0

  if a > b:
    max = a
  else:
    max = b

  if max > c:
    return max
  else:
    return c

print("1, 75, 4 - max: " + str(max_of_three(1,75,4)))
print("100, 1, 493 - max: " + str(max_of_three(100,1,493)))
print("1, 1, 1 - max: " + str(max_of_three(1,1,1)))