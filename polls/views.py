from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    nom = "Martial nouveau"
    return render(request,"index.html")
    

