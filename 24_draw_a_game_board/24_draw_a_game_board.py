#!/usr/bin/python3

VERT_SEGMENT = " ---"
HORI_SEGMENT = "|   "
HORI_END_SEGMENT = "|"

def draw_board(size_x, size_y):
  for _ in range(0,size_y):
    for _ in range(0,size_x):
      print(VERT_SEGMENT,end="")
    print("\n",end="")
    for _ in range(0,size_x):
      print(HORI_SEGMENT,end="")
    print(HORI_END_SEGMENT)
  for _ in range(0,size_x):
    print(VERT_SEGMENT,end="")

draw_board(7,7)