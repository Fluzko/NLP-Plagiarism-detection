from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
from src.models import *
from src import cfg
import src.repositories as repository
import src.services.utils as utils
import shutil
import json


class Detector:
    def __init__(self, file):
        self.embeddingsComputer = utils.EmbeddingsComputer()
        self.file = file
        self.timestamp = datetime.timestamp(datetime.now())
        self.tmp_file_name = f'{self.timestamp}@{self.file.filename}'
        self.tmp_dir = cfg.tmp_dir
        self.dataset_dir = cfg.dataset_dir
        self.full_path = f'{self.tmp_dir}/{self.timestamp}@{self.file.filename}'
        self.cosine_similarity_treshold = cfg.cosine_similarity_threshold
        self.jaccard_similarity_threshold = cfg.jaccard_similarity_threshold

    def detect(self):
        print(self.file)
        self.file.save(self.full_path)
        paragraphs = utils.Parser(self.full_path, '.').parse()
        if len(paragraphs):
            text_preprocessed = utils.Cleaner(paragraphs).preprocess()
            _bigrams = utils.NGramsCalculculator(text_preprocessed).get_bigrams()
            text_embeddings = self.embeddingsComputer.compute(text_preprocessed)
            self.__move_from_tmp_to_permanent__(self.full_path, f'{self.dataset_dir}/{self.file.filename}')
            suspected_text = repository.TextRepository(self.dataset_dir).save(self.file.filename, text_embeddings, _bigrams)
            texts = self.get_comparable_texts(suspected_text)
            plagirisms_detections = [self.get_plagiarism(suspected_text, _text) for _text in texts]
            return json.dumps([a.__dict__ for a in plagirisms_detections if a.may_be_plagiarism])
            # return json.dumps(max(plagirisms_detections, key=lambda x: x.plagiarism_percentage).__dict__)

    def get_plagiarism(self, suspected, _text):
        result = PlagiarismResult()
        result.file_name = _text.file_name
        if not self.may_be_plagiarism_of(suspected.bigrams_to_set(), _text.bigrams_to_set()):
            return result
        else:
            result.may_be_plagiarism = True
            plagiarised_features = self.plagiarised_sentences(suspected, _text)
            result.plagiarised_sentences = [plagiarised_feature.sentence for plagiarised_feature in plagiarised_features]
            result.plagiarism_percentage = len(plagiarised_features) / len(_text.features)
        return result

    @staticmethod
    def get_comparable_texts(some_text):
        return Text.query.all()

    @staticmethod
    def __move_from_tmp_to_permanent__(old_path, new_path):
        shutil.move(old_path, new_path)



    @staticmethod
    def jaccard_similarity_coefficient(suspect_n_grams, original_n_grams):
        return len(suspect_n_grams.intersection(original_n_grams)) / len(suspect_n_grams.union(original_n_grams))

    def may_be_plagiarism_of(self, suspect_bigrams, original_bigrams):
        coefficient = self.jaccard_similarity_coefficient(
            suspect_bigrams, original_bigrams)
        return coefficient > self.jaccard_similarity_threshold

    def sentence_is_semantically_similar(self, suspect_feature, original_feature):
        suspect_embedding = Feature.deserialize_embedding(suspect_feature.embedding)
        original_embedding = Feature.deserialize_embedding(original_feature.embedding)
        return cosine_similarity(suspect_embedding, original_embedding) >= self.cosine_similarity_treshold

    @staticmethod
    def any_match(collection, function):
        for element in collection:
            if function(element):
                return True
        return False

    def sentence_is_plagiarism(self, suspect_feature, original_features):
        return self.any_match(
            original_features,
            lambda original_feature: self.sentence_is_semantically_similar(suspect_feature, original_feature)
        )

    def plagiarised_sentences(self, suspect_text, original_text):
        return list(
            filter(
                lambda suspect_feature: self.sentence_is_plagiarism(suspect_feature, original_text.features),
                suspect_text.features
            )
        )

    def plagiarism_percentage(self, suspect_text, original_text, cosine_similarity_threshold=0.7):
        n_plagiarised = len(self.plagiarised_sentences(suspect_text, original_text, cosine_similarity_threshold))
        n_total = len(original_text.features)
        return n_plagiarised / n_total
