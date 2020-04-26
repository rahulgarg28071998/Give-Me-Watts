from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from .models import Placey

# Create your views here.
def home(request):
    context = {
    }
    return render(request,"index.html",context)

def bid(request):
    return render(request,"bid.html")

def response(request):
    context = {}
    return render(request,"home.html",context)

def recommendation_function(request,data):
    context = {}
    return JsonResponse(context,safe=False)

def recommend(request):
    context = {}
    return render(request,"recommend.html",context)