from nltk import sent_tokenize
from src import embed


class EmbeddingsComputer:
    def __init__(self):
        self.embed = embed

    def compute(self, text):
        text_embeddings = []
        for sent in sent_tokenize(text):
            text_embeddings.append((self.embed(sent).numpy().reshape(1, 512), sent))
        return text_embeddings
