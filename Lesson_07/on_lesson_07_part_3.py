import json
from pathlib import Path


class ExchangeRate:
    def __init__(self, from_: str, to_: str, value: float) -> None:
        self.from_: str = from_
        self.to_: str = to_
        self.value: float = value

    def __repr__(self) -> str:
        return f"{self.from_}-{self.to_}: {self.value}"


class ExchangeRatesService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargsa):
        if cls._instance:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename: Path) -> None:
        if self._initialized:
            return
        self.filename: Path = filename
        self.rates: list[ExchangeRate] = self._get_rates()
        self._initialized = True

    def _get_rates(self) -> list[ExchangeRate]:
        with open(self.filename) as file:
            print("READING FROM FILE...")
            raw_data: str = file.read()
            data: dict = json.loads(raw_data)

        return [
            ExchangeRate(
                from_=element["from_"],
                to_=element["to_"],
                value=element["value"],
            )
            for element in data["results"]
        ]


def main():
    FILENAME = Path(__file__).parent / "exchange_rates.json"
    er_service = ExchangeRatesService(FILENAME)
    # rates: list[ExchangeRate] = er_service.rates
    print(er_service.rates)


if __name__ == "__main__":
    main()
