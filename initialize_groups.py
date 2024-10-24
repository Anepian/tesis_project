import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tesis_project.settings')
django.setup()

from django.contrib.auth.models import User, Group

# Crear grupos si no existen
Group.objects.get_or_create(name='Students')
Group.objects.get_or_create(name='Professors')
Group.objects.get_or_create(name='Admins')

# Obtener el usuario
user = User.objects.get(username='profesor')

# Obtener el grupo
group = Group.objects.get(name='Professors')

# Asignar el usuario al grupo
user.groups.add(group)

print(f"Usuario {user.username} asignado al grupo {group.name}")