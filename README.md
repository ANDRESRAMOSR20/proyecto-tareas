# Proyecto de Tareas

Este proyecto es una aplicación de gestión de tareas construida con Python. Permite crear, listar, completar y eliminar tareas. También tiene soporte para almacenamiento en base de datos SQLite o en un archivo JSON, según la configuración. El proyecto incluye pruebas automatizadas y está integrado con SonarQube para el análisis de calidad del código.

## Requisitos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- SQLite (base de datos utilizada por defecto)
- SQLAlchemy (para la gestión de bases de datos)
- Streamlit (para la interfaz de usuario)

## Instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/ANDRESRAMOSR20/proyecto-tareas.git
cd proyecto-tareas
```
### 2. Crear un entorno virtual
Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Para crear y activar el entorno, usa los siguientes comandos:

En Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
En Linux o macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Instalar dependencias
Instala todas las dependencias necesarias para el proyecto utilizando pip:
```bash
pip install -r requirements.txt
```
### 4. Configuración de la base de datos
Este proyecto está configurado para usar SQLite por defecto, pero puedes cambiar la configuración para usar otro sistema de base de datos si es necesario. Para inicializar la base de datos, simplemente ejecuta el siguiente comando en un terminal de Python:
```bash
from database import init_db
init_db()
```
## Uso
### 1. Ejecutar la aplicación
Para ejecutar la aplicación, utiliza el siguiente comando:
```bash
python app.py
```
### 2. Ejecutar las pruebas
Para ejecutar las pruebas de la aplicación, utiliza pytest con el siguiente comando:
```bash
pytest
```
# Fin del Despliegue.
