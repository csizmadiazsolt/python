# !/usr/bin/python3

class FamilyNode:
  nodeCount = 0
  
  def __init__(self, name, birthday, deathday=None):
    self.name = name
    self.birthday = birthday
    self.deathday = deathday
    self.mother = None
    self.father = None
    self.children = []
    FamilyNode.nodeCount += 1
 
  def addFather(self, father):
    self.father = father

  def addMother(self, mother):
    self.mother = mother

  def addChild(self, child):
    self.children.append(child)