from django.shortcuts import render

# Create your views here.



def inicio(request):
    return render(request,'AppCoder/index.html')

def Universidad(request):
    return render(request,'AppCoder/universidad.html')

def Alumno(request):
    return render(request,'AppCoder/alumno.html')

def Docente(request):
    return render(request,'AppCoder/docente.html')

def Envio(request):
    return render(request,'AppCoder/envio.html')


