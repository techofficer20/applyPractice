from django.shortcuts import render, redirect
from .models import lecture
# Create your views here.

def index(request):
    lec_obj = lecture.objects.all()
    return render(request, 'index.html', {'lec_obj' : lec_obj})

def new(request):
    return render(request, 'new.html')

def create(request):
    lectures = lecture()
    lectures.grade = request.GET['grade']
    lectures.lec_num = request.GET['lec_num']
    lectures.lec_title = request.GET['lec_title']
    lectures.lec_num2 = request.GET['lec_num2']
    lectures.lec_value = request.GET['lec_value']
    lectures.lec_time = request.GET['lec_time']
    lectures.lec_prof = request.GET['lec_prof']
    lectures.lec_success = request.GET['lec_success']
    lectures.lec_limit = request.GET['lec_limit']
    lectures.lec_stair = request.GET['lec_stair']
    lectures.lec_time2 = request.GET['lec_time2']
    lectures.save()
    return redirect('index')