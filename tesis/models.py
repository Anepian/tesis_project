from django.contrib.auth.models import User
from django.db import models

class Thesis(models.Model):
    CATEGORY_CHOICES = [
        ('programacion', 'Programación'),
        ('redes', 'Redes'),
        ('seguridad', 'Seguridad'),
        ('iot', 'IoT'),
        ('big_data', 'Big Data'),
        ('inteligencia_artificial', 'Inteligencia Artificial'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    advisor = models.CharField(max_length=255)
    co_advisor = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    pdf = models.FileField(upload_to='theses/')
    visible = models.BooleanField(default=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Suponiendo que el ID del usuario administrador es 1

    def __str__(self):
        return self.title