from src import db
import numpy as np


class Feature(db.Model):
    __tablename__ = 'feature'
    id = db.Column(db.Integer, primary_key=True)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))
    text = db.relationship("Text", back_populates="features")

    sentence = db.Column(db.String, nullable=False)
    embedding = db.Column(db.String, nullable=False)

    @staticmethod
    def serialized_embedding(embedding_array):
        print(embedding_array)
        serialized_string = ''
        for e in embedding_array:
            serialized_string += str(e) + ','
        return serialized_string

    @staticmethod
    def deserialize_embedding(serialized_embedding):
        embeddings = serialized_embedding.split(',')
        embeddings.pop()
        return np.array(embeddings).reshape(1, 512)
