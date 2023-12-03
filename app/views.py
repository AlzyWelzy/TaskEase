from django.shortcuts import render, redirect
import datetime
from .models import App


# Create your views here.
def index(request):
    if request.method == "POST":
        app_name = request.POST.get("app_name")
        app_progress = request.POST.get("app_progress")
        print(app_name, app_progress)

        app = App()
        app.name = app_name
        app.progress = app_progress
        app.save()

        return redirect("/")

    queryset = App.objects.all()

    context = {
        "title": "Taskify",
        "apps": queryset,
        "year": datetime.datetime.now().year,
    }
    return render(request, "index.html", context)
