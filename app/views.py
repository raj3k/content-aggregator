from django.shortcuts import render
import feedparser


# Create your views here.
def index(request):
    return render(request, 'index.html', {})