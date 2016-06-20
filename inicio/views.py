from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html', {})


# Create your views here.
def cualquiercosa(request):
    return render(request, 'cualquiercosa.html', {})
