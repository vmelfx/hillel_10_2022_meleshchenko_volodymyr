from datetime import date
from typing import Any


class RentError(Exception):
    pass


class Car:
    def __init__(self, name: str, price: int, color: str) -> None:
        self.name = name
        self.price = price
        self.color = color

    def __str__(self) -> str:
        return f"{self.name}"


class User:
    def __init__(self, name: str, birthday: date) -> None:
        self.name: str = name
        self.birthday: date = birthday


class CarRent:
    def __init__(
        self, user: User, car: Car, duration: int, min_price: int = 300
    ) -> None:
        """
        :param duration: duration set in minutes
        """
        self.car: Car = car
        self.duration: int = duration
        self.user: User = user
        self.min_price: int = min_price
        self.__total_price: int = self.car.price * self.duration

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, value: Any):
        if not isinstance(value, int):
            raise RentError(f"The value {value} is not a valid integer")

        if value <= self.min_price:
            self.__total_price = self.min_price
        else:
            self.__total_price = value

    def book(self):
        print(
            f"Booking {self.car} for {self.duration} hours by {self.user.name}"
        )
        print(f"Total price: {self.total_price}")


class Discount:
    def __init__(self, rent: CarRent) -> None:
        self.rent: CarRent = rent

    def apply(self) -> None:
        today: date = date.today()
        bd: date = self.rent.user.birthday
        if (bd.month, bd.day) == (today.month, today.day):
            new_price: int = int(self.rent.total_price * 0.3)
            self.rent.total_price = new_price


def handle_base_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RentError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Occurred error: {error}")

    return inner


@handle_base_errors
def main():
    john = User(name="John", birthday=date(year=1990, month=11, day=15))

    vw = Car(name="Passat", price=200, color="blue")
    audi = Car(name="A6", price=300, color="black")

    rent = CarRent(user=john, car=audi, duration=3)
    rent_vw = CarRent(user=john, car=vw, duration=10)

    discount = Discount(rent)
    discount.apply()

    discount = Discount(rent_vw)
    discount.apply()

    rent.book()
    rent_vw.book()


main()
