import os
import src.services.utils as utils
from src.models import *
from src import cfg, db
import src.repositories as repository


class Preprocessor:
    def __init__(self):
        self.dataset_dir = cfg.dataset_dir
        self.embeddingsComputer = utils.EmbeddingsComputer()

    def start(self):
        all_file_names = os.listdir(self.dataset_dir)
        processed_texts = Text.query.all()
        not_processed_file_names = [file_name for file_name in all_file_names if file_name not in [textModel.file_name for textModel in processed_texts]]
        print(f'se van a procesar {len(not_processed_file_names)} de un total de {len(all_file_names)}')
        for file_name in not_processed_file_names:
            paragraphs = utils.Parser(file_name, self.dataset_dir).parse()
            if len(paragraphs):
                text_preprocessed = utils.Cleaner(paragraphs).preprocess()
                bigrams = utils.NGramsCalculculator(text_preprocessed).get_bigrams()
                text_embeddings = self.embeddingsComputer.compute(text_preprocessed)
                repository.TextRepository(self.dataset_dir).save(file_name, text_embeddings, bigrams)
