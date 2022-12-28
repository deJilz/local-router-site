from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
    
def bio(request):
    return render(request, 'bio.html', {})