from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    data={
        'title':"Home-Page",
        'list':['PHP','Python','Djnago'],
        'student_details':[
            {'name':'Yash','phone':8081452334},
            {'name':'Rakesh','phone':8808742978}
        ],
        'numbers':[10,20,30,40,50]
    }
    return render(request,"index.html",data)

def AboutUs(request):
    return HttpResponse("Welcome to our World")

def Course(request):
    return HttpResponse("Our Courses")

def Coursedetails(request,courseid):
    return HttpResponse(courseid)

