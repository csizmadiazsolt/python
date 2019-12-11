# !/usr/bin/python3
import family_node

class FamilyTree:
  numberOfSiblings = 0
  
  def getSiblings(familyNode):
    if getattr(familyNode, 'mother'):
      mother = getattr(familyNode, 'mother')
      siblings = getattr(mother, 'children')
      
      return siblings

  def printSiblings(self, familyNode):
    siblings = FamilyTree.getSiblings(familyNode)
    
    if familyNode in siblings:
      siblings.remove(familyNode)
    
    node_name = getattr(familyNode,'name')
    print("{}'s siblings:".format(node_name))
    print("-"*(len(node_name)+12))
    
    for sibling in siblings:
      sibling_name = getattr(sibling, 'name')
      sibling_birthday = getattr(sibling, 'birthday')
      print("{} - {}".format(sibling_name, sibling_birthday))

  def printNumberOfFamilyMembers(self):
    print("\nNumber of family members: {}".format(family_node.FamilyNode.nodeCount))

father = family_node.FamilyNode("Csizmadia József", "1955.08.12", "2014.05.12")
mother = family_node.FamilyNode("Horváth Márta", "1963.08.02")
nori = family_node.FamilyNode("Csizmadia Nóra", "1985.05.13")
zsolti = family_node.FamilyNode("Csizmadia Zsolt", "1987.12.01")
kazmer = family_node.FamilyNode("Csizmadia Kázmér", "1995.10.10")

zsolti.addMother(mother)
zsolti.addFather(father)
nori.addMother(mother)
nori.addFather(father)
kazmer.addMother(mother)
kazmer.addFather(father)

mother.addChild(zsolti)
mother.addChild(nori)
mother.addChild(kazmer)
father.addChild(zsolti)
father.addChild(nori)
father.addChild(kazmer)

tree = FamilyTree()
tree.printSiblings(zsolti)
tree.printNumberOfFamilyMembers()