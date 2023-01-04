from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
import json

import pickle
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd 
import os

module_dir = os.path.dirname(__file__)  # get current directory


def predict(phrase, model_filepath='model_pickled.pickle', vectorizer_filepath = 'vectorizer_pickled.pickle' ): 
    with open(os.path.join(module_dir, model_filepath), 'rb') as pickle_file:
        loaded_MNB = pickle.load(pickle_file)

    with open(os.path.join(module_dir, vectorizer_filepath), 'rb') as pickle_file:
        vectorizer = pickle.load(pickle_file)

    d = {0:phrase}
    ser = pd.Series(data=d)
    vector = vectorizer.transform(ser)

    prediction = loaded_MNB.predict(vector)

    if prediction[0] == 0: 
        return 'negative'
    else:
        return 'positive'

class PredicitonView(View):
    def get(self, request):
        return render(request, 'prediction/index.html')

class Score(View):
    def post(self, request):
        
        data = json.loads(request.body)#parsing post requet to json
        text = data['text']
        
        #load model 
        #make prediction with text
        sentiment = predict(text) 
        return JsonResponse({'sentiment': sentiment})
