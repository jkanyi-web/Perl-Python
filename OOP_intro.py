class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_hello(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old")


class1 = Person("Alice", 25)
class1.say_hello()
