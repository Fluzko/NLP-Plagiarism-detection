from src import db


class Text(db.Model):
    __tablename__ = 'text'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    file_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    features = db.relationship("Feature", back_populates="text")
    bigrams = db.relationship("Bigram", back_populates="text")

    def bigrams_to_set(self):
        return set([(bigram.first, bigram.second) for bigram in self.bigrams])

