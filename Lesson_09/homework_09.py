from dataclasses import dataclass

exchange_rates = {
    "base": "USD",
    "rates": {"USD": 1.00, "UAH": 0.025, "EUR": 1.05},
}


@dataclass()
class Price:
    amount: int
    currency: str

    def __post_init__(self):
        self.currency = self.currency.upper()

    def __add__(self, other: "Price"):
        if self.currency == "USD":
            return Price(self.amount + other.amount, self.currency)
        elif self.currency == "UAH":
            return ExchangeRatesService.convert(
                base_price=self
            ) + ExchangeRatesService.convert(base_price=other)
        elif self.currency == "EUR":
            return ExchangeRatesService.convert(
                base_price=self
            ) + ExchangeRatesService.convert(base_price=other)

    def __sub__(self, other: "Price"):
        if self.currency == "USD":
            return Price(self.amount - other.amount, self.currency)
        elif self.currency == "UAH":
            return ExchangeRatesService.convert(
                base_price=self
            ) - ExchangeRatesService.convert(base_price=other)
        elif self.currency == "EUR":
            return ExchangeRatesService.convert(
                base_price=self
            ) - ExchangeRatesService.convert(base_price=other)


class ExchangeRatesService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

    @staticmethod
    def convert(base_price: Price) -> Price:
        target_currency = exchange_rates["base"]

        if base_price.currency == "EUR":
            new_price = (
                base_price.amount
                * exchange_rates["rates"][base_price.currency]
            )
            return Price(amount=new_price, currency=target_currency)
        elif base_price.currency == "UAH":
            new_price = (
                base_price.amount
                * exchange_rates["rates"][base_price.currency]
            )
            return Price(amount=new_price, currency=target_currency)


def main():
    price_1 = Price(amount=10, currency="uah")
    price_2 = Price(amount=10000, currency="uah")
    price_3 = price_1 + price_2
    price_4 = price_1 - price_2

    print(price_3)
    print(price_4)


if __name__ == "__main__":
    main()
