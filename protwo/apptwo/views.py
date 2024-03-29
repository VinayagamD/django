from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import User


# Create your views here.
def index(request):
    return render(request, 'apptwo/index.html')


def help_page(request):
    help_dict = {'help_insert': 'HELP PAGE'}
    return render(request, "apptwo/help.html", context=help_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, "apptwo/users.html", context=user_dict)
