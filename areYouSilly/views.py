from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')
def truth(request):
    if request.method == 'POST':
        pass
        
    return render(request, 'truth.html')