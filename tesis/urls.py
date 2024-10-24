from django.urls import path
from . import views

app_name = 'tesis'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_thesis, name='upload_thesis'),
    path('toggle_visibility/<int:thesis_id>/', views.admin_toggle_visibility, name='admin_toggle_visibility'),
    path('theses/', views.visitor_view_theses, name='visitor_view_theses'),
    path('thesis/<int:thesis_id>/', views.thesis_detail, name='thesis_detail'),
]