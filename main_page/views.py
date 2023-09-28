from django.shortcuts import render
from .models import Project
def home(request):
    projects =Project.objects.all()

    return render(request, '/home/maxim/Desktop/putoran_website_project/putoran_website/templates/main_page/home_page.html', {'projects':projects})
# Create your views here.
