Este proyecto está hecho en python con el framework web Django, la API es de tipo REST, por lo cúal utilizo la librería Django Rest Framework, dandome la facilidad de habilitar endpoints para que puedan ser consumidos los servicios creados.

Este proyecto usa python, django, django-admin, django rest framework, postgres, pandas, whitenoise, git lfs, tests unitarios, funciones utilitarias, configuración de entorno local y producción, y variables de entorno para permitir la seguridad de la aplicación.

En primer lugar, para que el proyecto pueda ser ejecutado en local debe clonarse el proyecto, y a la altura del proyecto debe ser creado un entorno virtual, este entorno virtual es un espacio para poder albergar librerías, paquetes y dependencias sin que afecté el entorno global de desarrollo. Allí se encapsulará todos lo que necesita el proyecto. Se crea escribiendo virtualenv env en la cmd o powershell

En segundo lugar, Para que este proyecto pueda ser ejecutado en local deben ser creadas 6 variables de entorno en el computador, para crearlas basta buscar en el navegador del sistema operativo "env". Además de esas variables, debe ser creada una base de datos en el servidor local de postgres, puede usar cualquier gestor de base de datos, recomiendo pg admin, de allí es de donde se obtendrán los valores de las variables 2 a la 6.

Las variables de entorno son: 
  1. FRACTTAL_SECRET_KEY: Es la secret key del proyecto de django, pueden generar esa key acá https://djecrety.ir/
  2. USER_FRACTTAL: Es el usuario del servidor postgres donde está la bd local
  3. PASSWORD_FRACTTAL: Es la contraseña del servidor postgres donde está la bd local
  4. HOST_FRACTTAL: Es el host del servidor postgres donde está la bd local
  5. PORT_FRACTTAL: Es el puesto del servidor postgres donde está la bd local
  6. NAME_FRACTTAL: Es el nombre de la base de datos al interior del servidor postgres

En tercer lugar, sería bueno tener postman en el computador para probar las API's, thunder client también es una buena opción.

En cuarto lugar, debe ser ejecutado el comando python manage.py makemigrations, despues python manage.py migrate, por último python manage.py runserver

Finalizando, los endpoints son los siguientes

"localhost:8000" para el admin de django
"localhost:8000/swagger/" para la documentación de swagger
"localhost:8000/api/measurements/" para el GET y POST method como lo pidió la prueba.

Por último, no se pidió pero se habilitó un servicio para aceptar archivos csv dinamícos, puede ser subido cualquier archivo al endpoint "localhost:8000/api/measurements-update/" y lo analizará buscando los valores entre 20 y 30 en el sensor 07 y 47. 

Cualquier duda estaré atento, rbenprieto@outlook.com
