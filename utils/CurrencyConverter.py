class CurrencyConverter:
    def __init__(self):
        self.rates = {
            "USD": 1.0,
            "$": 1.0,
            "CAD": 1.32,
            "EUR": 0.92,
            "GBP": 0.78,
            "INR": 71.0,
            "AED": 3.67,
            "AUD": 1.47,
            "CAD": 1.32,
            "CHF": 0.99,
            "CNY": 7.07,
            "MYR": 4.19,
            "JPY": 108.62,
            "KRW": 1193.0,
            "SGD": 1.36,
            "NZD": 1.57,
            "BRL": 4.07,
            "RUB": 63.0,
            "TRY": 5.94,
            "ZAR": 14.6,
            "NOK": 9.0,
            "SEK": 9.6,
            "DKK": 6.7,
            "EUR": 0.92,
            "GBP": 0.78,
        }

    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another."""
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency.")
        return amount * (self.rates[to_currency] / self.rates[from_currency])