from django.shortcuts import render

# Create your views here.



def inicio(request):
    return render(request,'AppCoder/index.html')

def curso(request):
    return render(request,'AppCoder/curso.html')

def estudiante(request):
    return render(request,'AppCoder/estudiante.html')

def profesor(request):
    return render(request,'AppCoder/profesor.html')

def entregable(request):
    return render(request,'AppCoder/entregable.html')


