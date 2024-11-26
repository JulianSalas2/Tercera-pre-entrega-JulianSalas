from django.shortcuts import render , redirect
from .forms import DocenteForm , UniversidadForm , EnvioForm,AlumnoForm
from .models import Universidad , Docente , Alumno , Envio

# Create your views here.



def inicio(request):
    return render(request,'appcoder/index.html')


def agregar_universidad(request):
    if request.method == 'POST':
        form = UniversidadForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la universidad si es válido
            return redirect('lista_universidad')  # Redirige a otra página después de guardar
    else:
        form = UniversidadForm()


    return render(request, 'appcoder/agregar_universidad.html', {'form': form})


def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lista_alumno')
    else:
        form = AlumnoForm()
    return render(request,'appcoder/agregar_alumno.html',{'form':form})



def agregar_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('lista_envio')
    else:
        form = EnvioForm()
    return render(request,'appcoder/agregar_envio.html',{'form':form})


def agregar_docente(request):
    # 1. Comprobamos si el formulario ha sido enviado (POST).
    if request.method == 'POST':
        # 2. Creamos una instancia del formulario, pasándole los datos que han llegado en el POST.
        form = DocenteForm(request.POST)
        
        # 3. Validamos el formulario para asegurarnos de que los datos son correctos.
        if form.is_valid():
            # 4. Si el formulario es válido, guardamos la nueva instancia de Docente en la base de datos.
            form.save()  # Guarda los datos del formulario como un nuevo objeto Docente

            # 5. Después de guardar los datos, redirigimos a la página de lista de docentes.
            return redirect('lista_docente')  # Cambia la vista a 'lista_docentes'

    else:
        # 6. Si no es una petición POST (es decir, es una petición GET), creamos un formulario vacío.
        form = DocenteForm()

    # 7. Renderizamos la página con el formulario, para que el usuario pueda agregar un docente.
    return render(request, 'appcoder/agregar_docente.html', {'form': form})


#                                                 -------LISTAS-----------

def lista_docente(request):
    docente = Docente.objects.all()  # Obtiene todos los docentes
    return render(request, 'appcoder/lista_docente.html', {'docentes': docente})

def lista_alumno(request):
    alumno = Alumno.objects.all()
    return render(request, 'appcoder/lista_alumno.html',{'alumnos':alumno})


def lista_universidad (request):
    universidad = Universidad.objects.all()
    return render(request,'appcoder/lista_universidad.html',{'universidades':universidad})


def lista_envio(request):
    envio = Envio.objects.all()
    return render(request, 'appcoder/lista_envio.html',{'envios':envio})


#                       ----- BUSQUEDA DE UNIVERSIDADES METODO GET------



def buscar_universidades(request):
    """
    Vista para buscar universidades en la base de datos.
    Si el usuario proporciona un nombre, filtra por ese criterio.
    Si no hay búsqueda, muestra todas las universidades.
    """
    # Obtener el parámetro 'q' desde la URL. Si no existe, usar una cadena vacía por defecto.
    query = request.GET.get('q', '')

    # Si hay un término de búsqueda, buscar universidades cuyo nombre coincida parcialmente.
    if query:
        universidades = Universidad.objects.filter(nombre__icontains=query)  # Búsqueda insensible a mayúsculas/minúsculas
    else:
        universidades = Universidad.objects.all()  # Si no hay consulta, mostrar todas las universidades.

    # Renderizar la plantilla y enviar las universidades y la consulta como contexto.
    return render(request, 'appcoder/buscar_universidades.html', {'universidades': universidades, 'query': query})
