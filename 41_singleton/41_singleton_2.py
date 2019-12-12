# !/usr/bin/python3

class Singleton:
  __instance = None

  def __init__(self):
    if Singleton.__instance != None:
      raise Exception("This class is a singleton!")
    else:
      Singleton.__instance = self

  def getInstance():
    if Singleton.__instance == None:
      __instance = Singleton()
    return Singleton.__instance

s1 = Singleton()
s2 = Singleton.getInstance()
s3 = Singleton.getInstance()

print(s1)
print(s2)
print(s3)