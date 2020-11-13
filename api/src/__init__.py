from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
import tensorflow_text
import tensorflow_hub as hub
import nltk

app = Flask(__name__)

cfg = Config()
app.config['SECRET_KEY'] = cfg.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.db_uri

db = SQLAlchemy(app)
import src.models
db.create_all()

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")
nltk.download('punkt')
nltk.download('stopwords')


from src.routes import routes
