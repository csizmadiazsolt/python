# !/usr/bin/python3

class Animal:
  def __init__(self, name):
    print("A new animal created!")
    self.name = name

  def getName(self):
    return self.name

class Mammal(Animal):
  def __init__(self, name, numberOfLegs = 4):
    Animal.__init__(self, name)
    self.numberOfLegs = numberOfLegs

  def getInfo(self):
    print("{} has {} legs.".format(self.name, self.numberOfLegs))

class Bird(Animal):
  def __init__(self, name, numberOfLegs = 2, numberOfWings = 2):
    Animal.__init__(self, name)
    self.numberOfLegs = numberOfLegs
    self.numberOfWings = numberOfWings

  def getInfo(self):
    print("{} has {} legs and {} wings.".format(self.name, self.numberOfLegs, self.numberOfWings))

dog = Mammal("Rex")
whale = Mammal("Mr. Whale", 0)
blackbird = Bird("Blacky")

dog.getInfo()
whale.getInfo()
blackbird.getInfo()

