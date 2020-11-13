from src.services.utils.cleaner.business_cleaner import BusinessCleaner
from nltk.corpus import stopwords
from nltk import word_tokenize


class Cleaner:
    def __init__(self, paragraphs):
        self.business = BusinessCleaner
        self.paragraphs = paragraphs
        self.spanish_stopwords = stopwords.words('spanish')

    def preprocess(self):
        business_preprocessed_text = self.business(self.paragraphs).preprocess()
        return ' '.join([word.lower() for word in word_tokenize(business_preprocessed_text) if word.lower() not in self.spanish_stopwords])
