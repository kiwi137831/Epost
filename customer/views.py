from django.shortcuts import render
from django.shortcuts import render, render_to_response
# Create your views here.
def homepage(request):
    return render_to_response('CourierHomepage.html')

