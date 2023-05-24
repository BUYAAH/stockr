from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

leagues = {
    1: 'League of legends',
    2: 'League gym-class',
    3: 'Some league',
}

def index(request):
    return render(request, 'index.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def league(request, pk):
    context = {
        'league': leagues[pk]
    }
    return render(request, 'league.html', context)