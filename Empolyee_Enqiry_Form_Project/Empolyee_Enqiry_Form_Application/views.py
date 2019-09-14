from django.shortcuts import render
from .forms import Employee_Enquiry_Form
from .models import Employee_Enquiry_Data
from django.http.response import HttpResponse

def Employee_Enquiry_View(request):
    if request.method=="POST":
        eform=Employee_Enquiry_Form(request.POST)

        if eform.is_valid():
                first_name=request.POST.get('first_name','')
                last_name=request.POST.get('last_name','')
                email=request.POST.get('email','')
                mobile_no=request.POST.get('mobile_no','')
                qualification= request.POST.get('qualification', '')
                location = request.POST.get('location', '')
                skill = request.POST.get('skill', '')
                data=Employee_Enquiry_Data(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    mobile_no=mobile_no,
                    qualification=qualification,
                    location=location,
                    skill=skill,

                )
                data.save()
                eform=Employee_Enquiry_Form()
                return render(request,'submit.html')
        else:

                return HttpResponse('Invalid form')
    else:
        eform = Employee_Enquiry_Form()
        return render(request, 'contact.html', {'abc': eform})


def sunil(request):
    eform = Employee_Enquiry_Form()
    return render(request,'contact.html',{'abc': eform})

def add(request):
    a=10
    b=20
    c=a+b
    return HttpResponse(c)