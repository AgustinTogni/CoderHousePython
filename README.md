# CoderHousePython

Aplicación web desarrollada con **Python** y **Django** orientada a la gestión de una distribuidora, permitiendo administrar distintas entidades del negocio como productos, clientes y proveedores.

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
* SQLite

# 📌 Notas

* Asegúrate de tener **Python instalado** en tu sistema.
* Las dependencias del proyecto se encuentran en el archivo `requirements.txt`.