# Centro Médico - Proyecto Django

## Descripción

Este proyecto es una web para la gestión de un centro médico. Permite agregar especialidades, doctores y pacientes, y muestra un listado de doctores. La aplicación utiliza el patrón Model-View-Template (MVT) de Django.

## Estructura del Proyecto

- **centro_medico/**: Directorio principal del proyecto, que contiene `manage.py` y la configuración de Django.
- **centro_medico/centro_medico/**: Contiene archivos de configuración como `settings.py`, `urls.py` y `wsgi.py`.
- **centro_medico/gestion_medica/**: La aplicación del centro médico, que contiene modelos, vistas, formularios, URLs y la carpeta `templates` con los archivos HTML.
- **myenv/**: El entorno virtual del proyecto.

## Instalación y Ejecución

1. **Clonar el repositorio:**  
   Clona este proyecto en tu máquina.

2. **Crear y activar el entorno virtual:**  
   En la terminal, ve a la carpeta raíz del proyecto y ejecuta:

   ```bash
   python -m venv myenv

   ```

3. **Activar el entorno virtual**  
   .\myenv\Scripts\Activate.ps1

4. **instalar dependencias**  
   pip install django

5. **realizar migraciones**  
   cd centro_medico
   python manage.py makemigrations
   python manage.py migrate

6. **Ejecutar el servidor de desarollo**  
   python manage.py runserver

**Luego, abre tu navegador y visita http://127.0.0.1:8000/ para ver la aplicación en acción.**
