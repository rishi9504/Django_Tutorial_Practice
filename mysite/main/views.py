from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("New homepage! Wow so amazing")
# Create your views here.
