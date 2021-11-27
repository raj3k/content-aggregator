from django.shortcuts import render, redirect
from .models import PythonMediumContent, ProgrammingMediumContent
import feedparser


# Create your views here.
def index(request):
    python_medium_content = PythonMediumContent.objects.all()
    programming_medium_content = ProgrammingMediumContent.objects.all()
    context = {
        'py_content': python_medium_content,
        'programming_content': programming_medium_content,
    }
    return render(request, 'index.html', context)


def update_python_medium(request):
    feed = feedparser.parse('https://medium.com/feed/tag/python')

    for i in range(10):
        model = PythonMediumContent()
        data = feed.entries[i]

        model.title = data.title
        model.url = data.link
        # Image
        start_img_index = (data.summary).find('img')+9
        end_img_index = (data.summary).find('width')-2
        model.img = data.summary[start_img_index:end_img_index]

        model.save()
    return redirect('/')


def update_programming_medium(request):
    feed = feedparser.parse('https://medium.com/feed/tag/programming')

    for i in range(10):
        model = ProgrammingMediumContent()
        data = feed.entries[i]

        model.title = data.title
        model.url = data.link
        # Image
        start_img_index = (data.summary).find('img')+9
        end_img_index = (data.summary).find('width')-2
        model.img = data.summary[start_img_index:end_img_index]

        model.save()
    return redirect('/')