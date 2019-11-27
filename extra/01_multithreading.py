#!/usr/bin/python3
import _thread
import time
from random import randint

global_a = 0
global_b = 0

def increase(thread_name):
  global global_a
  global global_b

  while (global_a < 10 and global_b < 10):
    time.sleep(randint(1,20))

    if thread_name == "A":
      global_a += 1

    if thread_name == "B":
      global_b += 1
	  
def output_scheduler():
  global global_a
  global global_b

  while (global_a < 10 and global_b < 10):
    time.sleep(0.1)
    generate_output(global_a,global_b)

  if(global_a > global_b):
    print("\nThe winner is A! (" + str(global_a) + "-" + str(global_b) + ")")
  else:
    print("\nThe winner is B! (" + str(global_a) + "-" + str(global_b) + ")")

def generate_output(number_of_As, number_of_Bs):
  print("\rA: [", end="")
  print("#"*number_of_As,end="")
  print(" "*int(10-number_of_As),end="")
  print("] - B: [", end="")
  print("#"*number_of_Bs,end="")
  print(" "*int(10-number_of_Bs),end="")
  print("]",end="")
  
try:
   _thread.start_new_thread(increase, ("A", ))
   _thread.start_new_thread(increase, ("B", ))
   _thread.start_new_thread(output_scheduler, ())
except:
   print("Error: unable to start thread")
   
input()