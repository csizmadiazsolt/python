# !/usr/bin/python3

class Animal:
  numberOfAnimals = 0
  def __init__(self, name):
    Animal.numberOfAnimals += 1
    print("Animal {} created.".format(Animal.numberOfAnimals))
    self.name = name

  def getInfo(self):
    print("{} is the name of the animal.".format(self.name))

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

animal = Animal("Generopida")
dog = Mammal("Rex")
whale = Mammal("Mr. Whale", 0)
blackbird = Bird("Blacky")

animal.getInfo()
dog.getInfo()
whale.getInfo()
blackbird.getInfo()