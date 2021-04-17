import requests
from .models import CatFact
from django.http import HttpResponse

def get_cat_fact(request):
    response = requests.get('https://catfact.ninja/fact').jason()
    fact = response['fact']
    CatFact(fact=fact).save()
    return HttpResponse('ok')