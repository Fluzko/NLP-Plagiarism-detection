from src import app
import src.services as service
from flask import Response, request


@app.route("/preprocess", methods=['POST'])
def start():
    try:
        service.Preprocessor().start()
        return Response(status=200)
    except:
        return Response(status=500)


@app.route("/detect", methods=['POST'])
def detect():
    try:
        plagiarism = service.Detector(request.files['file']).detect()
        return plagiarism
    except:
        return Response(status=500)
