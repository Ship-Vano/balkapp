from django.urls import path
from . import views
app_name = 'work'
urlpatterns = [
    path('', views.create, name='work'),
    # path('', views.index, name = 'index'),
    #path('create/', views.create, name = 'create'),
]