from django.shortcuts import render, HttpResponse
from django.template import RequestContext

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Vinay Ganesh'
    args = {'myName':name, 'numbers':numbers}

    return render( request, 'accounts/home.html',args)