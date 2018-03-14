#
# Example file for working with classes
#

# Simple Base Class
class myClass():

  # NOTE: the first argument to any method in a class is "self" which refers
  # to the object itself
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

# Class that inherits from another class
class anotherClass(myClass):

  def method1(self):
    # invoke the base class method
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, someString):
    print("anotherClass method2 " + someString)


def main():
  c = myClass()
  c.method1()
  c.method2("This is a string")

  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string")

if __name__ == "__main__":
  main()
