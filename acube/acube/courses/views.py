from django.http import HttpResponse

def index(request):
    return HttpResponse("<center> <h1> Frontend development which includes reactJS <h1/> <center/>")

def fullstack(request):
    return HttpResponse("Fullstack web development for both python and java")

def backend(request):
    return HttpResponse("Data analysis, MySql etc")
