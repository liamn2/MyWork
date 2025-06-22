# A few notes on classes in Python.
class NameOfClass:                     
  def __init__(self, parameter):
    self.parameter = parameter

  def AnotherFunction(self):
    print("Output of AnotherFunction")

#In Python, a class serves as a blueprint for creating objects, which are instances of that class. They encapsulate data (attributes) and functions (methods) that operate on that data, promoting modular and organized code. 
#A class is defined using the class keyword, followed by the class name and a colon. Inside the class, attributes are defined as variables, and methods are defined as functions. The __init__ method is a special method, often called the constructor, used to initialize the object's attributes when an object is created.

# Binary Tree Class
#A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. It is a non-linear data structure, meaning that elements are not arranged sequentially like in an array or linked list. 
class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


class myClass:
  def __init__(self, String):
    self.val = String
    
