from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hellp World</h1>") # string of HTML code

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")