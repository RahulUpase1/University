""""
vegetables = input("What vegetable is actually a fruit? ")

def fruit(vegetables):
    fruits = ["apple", "banana", "cherry"]
    fruits.append(vegetables)
    for x in fruits:
        if x == "banana":
            continue
        print(x)

fruit(vegetables)
"""
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass


x = Student('Mike')
x.printname()