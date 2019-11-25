from flask import Flask, request, jsonify
from decouple import config
from flask_cors import CORS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


def create_app():
    app =Flask(__name__)
    CORS(app)

    sid = SentimentIntensityAnalyzer()

    @app.route('/')
    def root():
        pass
    
    @app.route('/sentiment',methods=["GET"])
   
    def sentiment():
        text = request.values['text']
        ss = sid.polarity_scores(text)
        return jsonify(ss)


    return app
