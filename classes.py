class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is Sleeping")


tiger = Animal("Tiger")
tiger.eat()
tiger.sleep()


# inheritance
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


dog = Dog("Dog")

dog.eat()
dog.bark()
dog.sleep()


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    # function overriding
    def sleep(self):
        print(f"{self.name} loves sleeping")


cat = Cat("Cat")
cat.eat()
cat.sleep()


class Person:
    def __init__(self):
        pass

    # instance method
    def instance_method(self):
        print("instance method is running", type(self))

    @staticmethod
    def static_method():
        print("static_method is Runnning")

    @classmethod
    def class_method(cls):
        print("class_method is Running", type(cls))


person = Person()
person.instance_method()
person.static_method()
person.class_method()

Person.static_method()
Person.class_method()
