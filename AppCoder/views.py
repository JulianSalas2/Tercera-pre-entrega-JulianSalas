from django.shortcuts import render , redirect
from .forms import DocenteForm , UniversidadForm , EnvioForm,AlumnoForm
from .models import Universidad , Docente , Alumno , Envio
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
# Create your views here.



def inicio(request):
    return render(request,'appcoder/index.html')

#                                           ClASES BASADAS EN VISTAS (CREAR / AGREGAR)

class UniversidadCreateView(CreateView):
    model = Universidad
    form_class = UniversidadForm
    template_name = "appcoder/agregar_universidad.html"
    success_url= reverse_lazy("lista_universidad")

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "appcoder/agregar_alumno.html"
    success_url= reverse_lazy("lista_alumno")
    
class DocenteCreateView(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = "appcoder/agregar_docente.html"
    success_url= reverse_lazy("lista_docente")
    
class EnvioCreateView(CreateView):
    model = Envio
    form_class = EnvioForm
    template_name = "appcoder/agregar_envio.html"
    success_url= reverse_lazy("lista_envio")

#                                           ClASES BASADAS EN VISTAS (Update / Editar )

class UniversidadUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Universidad
    form_class = UniversidadForm
    template_name = "appcoder/editar_universidad.html"
    success_url = reverse_lazy("lista_universidad")

class AlumnoUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Alumno
    form_class = AlumnoForm
    template_name = "appcoder/editar_alumno.html"
    success_url = reverse_lazy("lista_alumno")
    
class DocenteUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Docente
    form_class = DocenteForm
    template_name = "appcoder/editar_docente.html"
    success_url = reverse_lazy("lista_docente")
    
class EnvioUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Envio
    form_class = EnvioForm
    template_name = "appcoder/editar_envio.html"
    success_url = reverse_lazy("lista_envio")

#                                           ClASES BASADAS EN VISTAS (DELETE / Eliminar )

class UniversidadDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Universidad
    success_url = reverse_lazy("lista_universidad")  # URL de redirección después de eliminar un curso
    template_name = "appcoder/eliminar_universidad.html"  # Plantilla para confirmar la eliminación
    
class AlumnoDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Alumno
    success_url = reverse_lazy("lista_alumno")  # URL de redirección después de eliminar un curso
    template_name = "appcoder/eliminar_alumno.html"  # Plantilla para confirmar la eliminación
    
class DocenteDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Docente
    success_url = reverse_lazy("lista_docente")  # URL de redirección después de eliminar un curso
    template_name = "appcoder/eliminar_docente.html"  # Plantilla para confirmar la eliminación
    
class EnvioDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Envio
    success_url = reverse_lazy("lista_envio")  # URL de redirección después de eliminar un curso
    template_name = "appcoder/eliminar_envio.html"  # Plantilla para confirmar la eliminación


#                                           ClASES BASADAS EN VISTAS ( List /Listas  )


class UniversidadDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Universidad
    template_name = "appcoder/detalle_universidad.html"
    
    
class AlumnoDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Alumno
    template_name = "appcoder/detalle_alumno.html"
    
    
class DocenteDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Docente
    template_name = "appcoder/detalle_docente.html"
    

class EnvioDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Envio
    template_name = "appcoder/detalle_envio"

#                                           ClASES BASADAS EN VISTAS ( List /Listas  )

class UniversidadListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Universidad  # Modelo con el que trabaja esta vista
    template_name = "appcoder/lista_universidad.html"  # Plantilla para renderizar la lista
    
class AlumnoListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Alumno  # Modelo con el que trabaja esta vista
    template_name = "appcoder/lista_alumno.html"  # Plantilla para renderizar la lista
    
class DocenteListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Docente  # Modelo con el que trabaja esta vista
    template_name = "appcoder/lista_docente.html"  # Plantilla para renderizar la lista
    
class EnvioListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Envio  # Modelo con el que trabaja esta vista
    template_name = "appcoder/lista_envio.html"  # Plantilla para renderizar la lista


#                                                 -------LISTAS-----------

# def lista_docente(request):
#     docente = Docente.objects.all()  # Obtiene todos los docentes
#     return render(request, 'appcoder/lista_docente.html', {'docentes': docente})

# def lista_alumno(request):
#     alumno = Alumno.objects.all()
#     return render(request, 'appcoder/lista_alumno.html',{'alumnos':alumno})


# def lista_universidad (request):
#     universidad = Universidad.objects.all()
#     return render(request,'appcoder/lista_universidad.html',{'universidades':universidad})


# def lista_envio(request):
#     envio = Envio.objects.all()
#     return render(request, 'appcoder/lista_envio.html',{'envios':envio})


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
