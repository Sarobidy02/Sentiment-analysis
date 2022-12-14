from django.shortcuts import render
from django.views import View
# Create your views here.
class EvaluationView(View):
    def get(self, request):
        #load a trained model
        #load test data
        #make prediction and generate score
        context = {'precision': 12, 'recall': 13, 'accuracy': 11, 'fone': 33}
        return render(request, 'evaluation/evaluation.html', context = context)
