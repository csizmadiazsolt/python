# !/usr/bin/python3

class Singleton:
  def __new__(self):
    if not hasattr(self, 'instance'):
      self.instance = super().__new__(self)
    return self.instance

s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

print(s1)
print(s2)
print(s3)