from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainApp/index.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values':['Даша Ланцева', '+5535258690','dashalan@gmail.com']})
