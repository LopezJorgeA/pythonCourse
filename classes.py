class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("woof")
marce = Dog("Marce", 1)
print(marce.name)
print(marce.age)
marce.bark()
marce.walk()
