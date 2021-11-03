from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def nido_servizi(request):
    return render(request, 'frontend/nido_servizi.html')

def nido_regolamento(request):
    return render(request, 'frontend/nido_regolamento.html')

def primavera_servizi(request):
    return render(request, 'frontend/primavera_servizi.html')

def primavera_regolamento(request):
    return render(request, 'frontend/primavera_regolamento.html')

def ptof(request):
    return render(request, 'frontend/ptof.html')

def documentazione(request):
    return render(request, 'frontend/documentazione.html')
