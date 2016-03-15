from django.shortcuts import render

# Create your views here.

def listar_recintos(request,pk):
	print ('sdfd', pk)	
	return render(request, 'recinto/recinto.html', {})

