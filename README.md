Tercera Pre-Entrega Julian Salas
Nota: tengo que decir que todo el trabajo lo hice desde la rama feature/new-code 
README: Guía de Uso y Prueba del Proyecto

Introducción

Este proyecto implementa un sistema de gestión con funcionalidades básicas para agregar, listar y buscar registros de universidades, alumnos, docentes y envíos.

A continuación, se detalla el orden recomendado para probar las funcionalidades, indicando dónde encontrarlas en el proyecto.
Iniciar el Proyecto en Localhost
Asegúrate de que el servidor de Django esté en funcionamiento: Si no has arrancado el servidor, abre una terminal y navega al directorio del proyecto, luego ejecuta el siguiente comando:

bash
Copiar código
python manage.py runserver
Accede a la aplicación en tu navegador: Abre un navegador web y accede a http://127.0.0.1:8000/ (o http://localhost:8000/).

Orden para Probar las Funcionalidades en Localhost
1. Página de Inicio
URL: http://127.0.0.1:8000/inicio/
Vista asociada: views.inicio
Descripción: Página principal del sistema donde puedes navegar a las demás funcionalidades del proyecto.
2. Formularios para Agregar Datos (POST)
Estos formularios permiten agregar nuevos registros a la base de datos.

Agregar Universidades:

URL: http://127.0.0.1:8000/agregar_universidad/
Vista asociada: views.agregar_universidad
Descripción: Formulario para registrar una nueva universidad (nombre y país).
Agregar Alumnos:

URL: http://127.0.0.1:8000/agregar_alumno/
Vista asociada: views.agregar_alumno
Descripción: Formulario para registrar nuevos alumnos (nombre, apellido, correo electrónico e ID).
Agregar Docentes:

URL: http://127.0.0.1:8000/agregar_docente/
Vista asociada: views.agregar_docente
Descripción: Formulario para registrar docentes (nombre, apellido, correo electrónico y profesión).
Agregar Envíos:

URL: http://127.0.0.1:8000/agregar_envio/
Vista asociada: views.agregar_envio
Descripción: Formulario para registrar envíos (nombre, descripción, fecha de entrega y estado de entrega).
3. Listar Registros (GET)
Las siguientes páginas muestran todos los registros de la base de datos.

Lista de Universidades:

URL: http://127.0.0.1:8000/lista_universidad/
Vista asociada: views.lista_universidad
Descripción: Muestra todas las universidades registradas con su nombre y país.
Lista de Alumnos:

URL: http://127.0.0.1:8000/lista_alumno/
Vista asociada: views.lista_alumno
Descripción: Muestra todos los alumnos registrados.
Lista de Docentes:

URL: http://127.0.0.1:8000/lista_docente/
Vista asociada: views.lista_docente
Descripción: Muestra todos los docentes registrados.
Lista de Envíos:

URL: http://127.0.0.1:8000/lista_envio/
Vista asociada: views.lista_envio
Descripción: Muestra todos los envíos registrados.
4. Búsqueda de Universidades (GET)
URL: http://127.0.0.1:8000/buscar_universidades/
Vista asociada: views.buscar_universidades
Descripción: Permite buscar universidades por nombre. Muestra los resultados que coinciden con la búsqueda de universidad.
Estructura de Archivos Clave
urls.py: Define todas las rutas del proyecto, conectando URLs con vistas específicas.
views.py: Contiene la lógica de las vistas, como formularios para agregar datos, búsqueda y listas.
models.py: Define los modelos de datos (Universidades, Alumnos, Docentes, Envíos).
forms.py: Implementa los formularios asociados a los modelos.
Plantillas (Templates):
appcoder/agregar_universidad.html: Formulario para agregar universidades.
appcoder/lista_universidad.html: Lista de universidades registradas.
appcoder/buscar_universidades.html: Página para buscar universidades.
Recomendaciones de Prueba
Agregar datos:

Dirígete a las URLs de los formularios (/agregar_universidad/, /agregar_alumno/, etc.) para registrar datos en la base de datos.
Listar datos:

Accede a las URLs de las listas de registros (/lista_universidad/, /lista_alumno/, etc.) para verificar que los datos se hayan almacenado correctamente.
Buscar datos:

Usa la funcionalidad de búsqueda (/buscar_universidades/) para comprobar que puedes filtrar universidades por nombre.
