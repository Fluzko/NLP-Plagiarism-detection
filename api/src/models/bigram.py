from src import db


class Bigram(db.Model):
    __tablename__ = 'bigram'
    id = db.Column(db.Integer, primary_key=True)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))
    text = db.relationship("Text", back_populates="bigrams")

    first = db.Column(db.String)
    second = db.Column(db.String)