from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def newcourse(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        context = {
            'course_name': request.POST['name'],
            'course_description': request.POST['description'],
        }
        return render(request, 'index.html', context)
    else:
        Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description'])
        messages.success(request, "Course succesfully created")
        return redirect('/')
    
def areyousure(request, idn):
    context = {
        'this_course': Course.objects.get(id=idn),
    }
    return render(request, 'areyousure.html', context)

def destroy(request, idn):
    this_course = Course.objects.get(id=idn)
    this_course.delete()
    return redirect('/')