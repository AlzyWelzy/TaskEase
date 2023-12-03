from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    context = {"title": "Taskify", "year": datetime.datetime.now().year}
    return render(request, "index.html", context)
