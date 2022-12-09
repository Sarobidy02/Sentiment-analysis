from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
import json

class PredicitonView(View):
    def get(self, request):
        return render(request, 'prediction/index.html')

class Score(View):
    def post(self, request):
        
        data = json.loads(request.body)#parsing post requet to json
        text = data['text']
        print(text)
        
        #load model 
        #make prediction with text
        sentiment = 'Negative'
        proba = 68
        return JsonResponse({'sentiment': sentiment, 'proba': proba})
