from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "text_app/index.html")


def counter(request):
    text = request.POST['text']
    count = len(text.split())
    return render(request, "text_app/counter.html", {'count': count})
