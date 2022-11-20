from functools import singledispatchmethod


class Person:
    __slots__ = ("name", "age")

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    @singledispatchmethod
    def greeting(self, text: str):
        print(f"Hello, your text is {text}")

    @greeting.register
    def _(self, text: int):
        print("Wow. This is a number")


john = Person(name="John", age=20)


# print(john.name)
# john.get_name()
john.greeting(123)
