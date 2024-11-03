# polymorpism is the ability to call the same method on different objects and have each object respond in a way that is appropriate for it.

class Dog:
    def speak(self):
        return "Woof!"
      
class Cat:
    def speak(self):
        return "Meow!"
      
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
