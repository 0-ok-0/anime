from django.shortcuts import render

def index(request):
    return render(request, 'anime/index.html')

def topAnime    (request):
    return render(request, 'anime/topAnime.html')