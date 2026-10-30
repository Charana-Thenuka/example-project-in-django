# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Charana";
    age = 15;
    marks = 40;
    is_member = True;

    context = {
        'username':name,
        'user_age':age,
        'marks': marks,
        'membership': is_member
    }

    return render(request, 'students/home.html', context);

# about page
def about(request):

    subjects = ["Mathamatics", "Science", "English", "History", "IT", "Buddihsum", "Commerce"];
    # subjects = [];

    context = {
        'subjects': subjects,
    }

    return render(request, 'students/about.html', context);

def contact(request):
    return render(request, 'students/contact.html');

def service(request):
    return render(request, 'students/service.html');