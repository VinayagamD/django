from django.shortcuts import render
from . import forms


# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, "basicapp/index.html", context=context_dict)


def other(request):
    return render(request, "basicapp/other.html")


def relative(request):
    return render(request, "basicapp/relative_url_templates.html")


def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid() :
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS")
            print("Name = "+form.cleaned_data['name'])
            print("Email = "+form.cleaned_data['email'])
            print("Text = "+form.cleaned_data['text'])
    return render(request, 'basicapp/form_page.html', {'form': form})
