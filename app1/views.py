from django.shortcuts import render

# Create your views here.
def img(request):
    return render(request, 'img.html')