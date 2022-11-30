from uuid import UUID

from providers import PayPalAPI


class User:
    def __init__(self, name: str) -> None:
        self.name = name


class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


def authorize_in_paypal(user: User) -> UUID:
    token: UUID = PayPalAPI.get_token()
    print(f"Authorized with PayPal...\n\tToken={token}")
    return token


def checkout_with_paypal(token: UUID, user: User, product: Product):
    print(
        f"{user.name} is buying {product.name} for "
        f"{product.price}$ with Stripe..."
    )


def checkout_with_stripe(user: User, product: Product):
    print(f"{user.name} is paying with Stripe...")


def main():
    john = User(name="John")
    microphone = Product(name="Razer", price=1000)
    payment_type = input("Enter payment type: ")

    if payment_type == "paypal":
        paypal_token: UUID = authorize_in_paypal(john)
        checkout_with_paypal(paypal_token, john, microphone)
    elif payment_type == "stripe":
        pass
    # pay_with_stripe(john, microphone)


if __name__ == "__main__":
    main()
