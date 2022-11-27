from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say_hello(self):
        raise NotImplementedError


class Dog(Animal):
    def say_hello(self):
        print("I am a dog")


class Cat(Animal):
    def say_hello(self):
        print("I am a cat")


jack = Dog()
jack.say_hello()

tom = Cat()
tom.say_hello()
