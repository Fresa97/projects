# projects
My projects
Gestión de Delegados al Congreso de la UJC
Este es un proyecto desarrollado en Python utilizando el framework de Django para gestionar la información de los delegados al Congreso de la Unión de Jóvenes Comunistas (UJC).

Descripción del proyecto
El objetivo de este proyecto es permitir a los organizadores del Congreso de la UJC gestionar la información de los delegados que asistirán al evento. El sistema permite registrar a los delegados, incluyendo su información personal, la organización a la que pertenecen y su posición dentro de la organización. Además, se pueden gestionar las credenciales de acceso al evento y la asignación de habitaciones en el lugar de hospedaje.

Requisitos del sistema
Este proyecto ha sido desarrollado utilizando Python 3.8 y Django 3.2. Los requisitos del sistema incluyen:

Python 3.8 o superior
Django 3.2 o superior
Otros paquetes de Python, que se encuentran listados en el archivo requirements.txt
Instalación y configuración
Para instalar el proyecto en tu entorno local, sigue los siguientes pasos:

Clona el repositorio desde GitHub:

Copy
git clone https://github.com/Fresa97/Projects.git
Crea un entorno virtual para el proyecto e instala las dependencias:

basic
Copy
cd gestion-delegados-ujc
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Crea la base de datos y las tablas necesarias:

Copy
python manage.py migrate
Carga los datos de ejemplo en la base de datos (opcional):

Copy
python manage.py loaddata delegados.json
Inicia el servidor de desarrollo:

Copy
python manage.py runserver
Abre tu navegador web y accede a la dirección http://localhost:8000 para ver la página principal del sistema.

Contribuciones
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

Haz un fork de este repositorio en GitHub.

Clona tu fork en tu entorno local.

Crea una nueva rama para tus cambios:

Copy
git checkout -b mi-rama-de-cambios
Realiza tus cambios y haz commit de los mismos:

Copy
git commit -am "Agrego una nueva funcionalidad"
Haz push de tus cambios a tu fork en GitHub:

Copy
git push origin mi-rama-de-cambios
Crea un pull request en GitHub desde tu rama de cambios hacia la rama master de este repositorio.

Espera a que los revisores del proyecto revisen tu pull request y hagan comentarios o soliciten cambios.

Una vez que tu pull request ha sido aprobado, haz merge de tus cambios en la rama master:

Copy
git checkout master
git pull origin master
git merge mi-rama-de-cambios
git push origin master
