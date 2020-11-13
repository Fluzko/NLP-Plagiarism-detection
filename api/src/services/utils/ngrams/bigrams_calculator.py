from nltk import bigrams, word_tokenize


class BigramCalculator:
    def __init__(self, text):
        self.text = text

    def calculate(self):
        return set(bigrams(word_tokenize(self.text)))
