#!/usr/bin/python3
from random import randint

LIST_MAX_LENGTH = 20
LIST_MAX_VALUE = 100

list_a_length = randint(1,LIST_MAX_LENGTH)
list_b_length = randint(1,LIST_MAX_LENGTH)

a = []
b = []
overlap = []

count = 0
while (count < list_a_length):
  a.append(randint(0,LIST_MAX_VALUE))
  count = count + 1

count = 0
while (count < list_b_length):
  b.append(randint(0,LIST_MAX_VALUE))
  count = count + 1

print("List A: " + str(a))
print("List B: " + str(b))

for element in a:
  if element in b:
    if element not in overlap: overlap.append(element)

print("Overlap: " + str(overlap))