from django.urls import path
from . import views
app_name = 'spring'
urlpatterns = [
    path('', views.create, name='spring'),
]