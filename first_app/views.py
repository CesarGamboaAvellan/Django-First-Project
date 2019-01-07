from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello im from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)
def test_function(request):
    test_function = {'test_me': "Testing url mapping and all that"}
    return render(request, 'test_templates/test.html', context=test_function)