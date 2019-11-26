#!/usr/bin/python3
import _thread
import time
from random import randint

LIST_MAX_VALUE = 2

def increase(thread_name):
  a = 0
  b = 0

  while a < 10:
    time.sleep(randint(0,LIST_MAX_VALUE))

    if thread_name == "A":
      a = a + 1
    else:
      b = b + 1

    generate_output(a,b)

def generate_output(number_of_As, number_of_Bs):
  print("\rA: [", end="")
  print("#"*number_of_As,end="")
  print(" "*int(10-number_of_As),end="")
  print("] - B: [", end="")
  print("#"*number_of_Bs,end="")
  print(" "*int(10-number_of_Bs),end="")
  print("]",end="")
  
generate_output(0,0)
  
try:
   _thread.start_new_thread( increase, ("A", ) )
except:
   print("Error: unable to start thread")
   
while 1:
  pass