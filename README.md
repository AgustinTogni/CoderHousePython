# CoderHousePython

## 🔋Terminado🔋
Este proyecto se encuentra finalizado, sin embargo, puede sufrir algunas modificaciones posteriores, ya sea por errores encontrados, optimización, cambios de versión, entre otros.

Estoy abierto a recibir cualquier tipo de sugerencia, corrección o consejo de quien quiera darlo. A su vez, no tengo problema en responder dudas o preguntas sobre el proyecto, puedes hacérmelas a través de cualquiera de los medios que tengo disponible en mi perfil.

# 📰Descripcion📰
Aplicación web desarrollada con **Python** y **Django** orientada a la gestión de una distribuidora, permitiendo administrar las principales entidades del negocio de forma centralizada.

La aplicación está organizada en distintos módulos que cubren las operaciones clave:

- **Productos**: alta, baja, modificación y consulta de productos (CRUD completo).
- **Clientes**: gestión integral de clientes con operaciones CRUD.
- **Proveedores**: administración de proveedores con funcionalidades CRUD.
- **Cuentas**:
  - Registro de usuarios  
  - Visualización de perfil  
  - Edición de datos personales 

El sistema permite trabajar de manera estructurada sobre cada entidad, facilitando la organización de la información y el mantenimiento de los datos dentro de la distribuidora.

# 🚀 Instalación y ejecución del proyecto

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

## 1. Clonar el repositorio

```bash
git clone https://github.com/AgustinTogni/CoderHousePython.git
```

## 2. Navegar al directorio del proyecto

```bash
cd CoderHousePython
```

## 3. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

## 4. Activar el entorno virtual

```bash
venv\Scripts\activate
```

## 5. Instalar las dependencias

Instalar todas las librerías necesarias definidas en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

## 6. Aplicar migraciones

Este paso crea las tablas necesarias en la base de datos.

```bash
python manage.py migrate
```

## 7. Ejecutar el servidor

Iniciar el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

# 🌐 Acceder a la aplicación

Una vez iniciado el servidor, abrir el navegador en:

```
http://127.0.0.1:8000/
```

Panel de administración:

```
http://127.0.0.1:8000/admin
```

# 🛠 Tecnologías utilizadas

* Python
* Django
* Bootstrap
* SQLite

# 📌 Notas

* Asegúrate de tener **Python instalado** en tu sistema.
* Las dependencias del proyecto se encuentran en el archivo `requirements.txt`.