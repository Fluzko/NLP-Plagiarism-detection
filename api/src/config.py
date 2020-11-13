import os


class Config:
    def __init__(self):
        self.db_uri = None
        self.secret_key = None
        self.dataset_dir = None
        self.tmp_dir = None
        self.threads_qty = None
        self.cosine_similarity_threshold = None
        self.jaccard_similarity_threshold = None

        if os.getenv('PRODUCTION_MODE'):
            self.prodConfig()
        else:
            self.devConfig()

    def prodConfig(self):
        self.db_uri = os.getenv('DB_URI')
        self.secret_key = os.getenv('SECRET_KEY')
        self.dataset_dir = os.getenv('DATASET_DIR')
        self.tmp_dir = os.getenv('TMP_DIR')
        self.threads_qty = os.getenv('THREADS')
        self.cosine_similarity_threshold = os.getenv('COSINE_SIMILARITY_THRESHOLD')
        self.jaccard_similarity_threshold = os.getenv('JACCARD_SIMILARITY_THRESHOLD')

    def devConfig(self):
        self.db_uri = 'sqlite:///site.db'
        self.secret_key = 'super-secret'
        self.dataset_dir = '../dataset'
        self.tmp_dir = '../tmp'
        self.threads_qty = 4
        self.cosine_similarity_threshold = 0.7
        self.jaccard_similarity_threshold = 0.2

