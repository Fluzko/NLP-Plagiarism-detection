from src.services.utils.ngrams.bigrams_calculator import BigramCalculator


class NGramsCalculculator:
    def __init__(self, text):
        self.text = text

    def get_bigrams(self):
        return BigramCalculator(self.text).calculate()
