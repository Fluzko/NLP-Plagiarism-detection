import src.models as models
from src import db


class TextRepository:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir

    def save(self, file_name, embeddings_sent_array, bigrams):
        new_text = models.Text()
        new_text.title = 'un titulo'
        new_text.file_name = file_name
        new_text.location = self.dataset_dir
        for emb_sent in embeddings_sent_array:
            new_text_feature = models.Feature()
            new_text_feature.sentence = emb_sent[1]
            new_text_feature.embedding = models.Feature.serialized_embedding(emb_sent[0][0])
            new_text.features.append(new_text_feature)

        for _bigram in bigrams:
            new_bigram = models.Bigram()
            new_bigram.first = _bigram[0]
            new_bigram.second = _bigram[1]
            new_text.bigrams.append(new_bigram)

        db.session.add(new_text)
        db.session.commit()
        return new_text