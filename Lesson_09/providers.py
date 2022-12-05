from uuid import UUID, uuid4


class PayPalAPI:
    @staticmethod
    def get_token() -> UUID:
        return uuid4()

    @staticmethod
    def buy(product_name: str, token: UUID) -> UUID:
        # ...
        return uuid4()


class StripeAPI:
    @staticmethod
    def get_token() -> UUID:
        return uuid4()

    @staticmethod
    def checkout(product_name: str, price: float, token: UUID) -> UUID:
        # ...
        return uuid4()
