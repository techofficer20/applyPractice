from django.shortcuts import render
from .models import lecture
# Create your views here.

def index(request):
    lec_obj = lecture.objects.all()
    return render(request, 'index.html', {'lec_obj' : lec_obj})