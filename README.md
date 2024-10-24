# Plataforma de Gestión de Tesis

Este proyecto es una plataforma de gestión de tesis para la Facultad de Telemática. Permite a los usuarios subir, modificar y visualizar tesis. Los superusuarios tienen acceso a todas las tesis subidas por todos los usuarios y pueden gestionar la visibilidad de las mismas.

## Características

- Subir y modificar tesis.
- Visualizar tesis disponibles.
- Búsqueda avanzada por título, autor, asesor, categoría, etc.
- Gestión de visibilidad de tesis por superusuarios.

## Requisitos

- Python 3.8+
- Django 5.1+

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/plataforma-tesis.git
    cd plataforma-tesis
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario:

    ```bash
    python manage.py createsuperuser
    ```

6. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

- Accede a la plataforma en `http://127.0.0.1:8000/`.
- Inicia sesión con el superusuario creado.
- Sube y modifica tesis desde la sección "Modificar Tesis".
- Visualiza las tesis disponibles desde la sección "Ver Tesis".
- Los superusuarios pueden gestionar la visibilidad de las tesis.

## Tests

Para ejecutar los tests, utiliza el siguiente comando:

```bash
python manage.py test