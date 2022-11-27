from uuid import UUID, uuid4


class PayPalAPI:
    @staticmethod
    def get_token() -> UUID:
        return uuid4()


class StripeAPI:
    @staticmethod
    def get_token() -> UUID:
        return uuid4()
