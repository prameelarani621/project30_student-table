from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def Student_form(request):
    ESFO=Student_form()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=Student_form(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('student_form done')
        else:
            return HttpResponse('invalid')
    
    return render(request,'Student_form.html',d)