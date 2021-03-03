from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    # return HttpResponse("<h2>Hello world!</h2>")
    return(request, "index.html")