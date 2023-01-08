from django.shortcuts import render
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ganre = request.POST.get('ganre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        link = request.POST.get('link')
        if request.FILES:

            image_file = request.FILES['image']
            if name and ganre and type and year and link:
            
                fss = FileSystemStorage()
                file = fss.save('app1/' + image_file.name, image_file)
                Film.objects.create(name=name,ganre=ganre, type=type, year=year, link=link, image=fss.url(file))
    films = Film.objects.all()
    context ={
        'films' : films
    }
    return render(request, 'app1/home.html', context)

def film(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ganre = request.POST.get('ganre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        link = request.POST.get('link')
        if request.FILES:

            image_file = request.FILES['image']
            if name and ganre and type and year and link:
            
                fss = FileSystemStorage()
                file = fss.save('app1/' + image_file.name, image_file)
                Film.objects.create(name=name,ganre=ganre, type=type, year=year, link=link, image=fss.url(file))
    films = Film.objects.filter(type="film")
    context = {
        'films' : films
    }
    return render(request, 'app1/home.html', context)

def serial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ganre = request.POST.get('ganre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        link = request.POST.get('link')
        if request.FILES:

            image_file = request.FILES['image']
            if name and ganre and type and year and link:
            
                fss = FileSystemStorage()
                file = fss.save('app1/' + image_file.name, image_file)
                Film.objects.create(name=name,ganre=ganre, type=type, year=year, link=link, image=fss.url(file))
    serials = Film.objects.filter(type="sereal")
    context = {
        'films' : serials
    }
    return render(request, 'app1/home.html', context)

def cartoon_sereal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ganre = request.POST.get('ganre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        link = request.POST.get('link')
        if request.FILES:

            image_file = request.FILES['image']
            if name and ganre and type and year and link:
            
                fss = FileSystemStorage()
                file = fss.save('app1/' + image_file.name, image_file)
                Film.objects.create(name=name,ganre=ganre, type=type, year=year, link=link, image=fss.url(file))
    cartoon_sereals = Film.objects.filter(type="cartoon_sereal")
    context = {
        'films' : cartoon_sereals
    }
    return render(request, 'app1/home.html', context)

def cartoon_film(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ganre = request.POST.get('ganre')
        type = request.POST.get('type')
        year = request.POST.get('year')
        link = request.POST.get('link')
        if request.FILES:

            image_file = request.FILES['image']
            if name and ganre and type and year and link:
            
                fss = FileSystemStorage()
                file = fss.save('app1/' + image_file.name, image_file)
                Film.objects.create(name=name,ganre=ganre, type=type, year=year, link=link, image=fss.url(file))
    cartoon_films = Film.objects.filter(type="cartoon_film")
    context = {
        'films' : cartoon_films
    }
    return render(request, 'app1/home.html', context)