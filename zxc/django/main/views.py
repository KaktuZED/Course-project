from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def prog(request):
    return render(request, 'main/prog.html')

def quest(request):
    return render(request, 'main/quest.html')