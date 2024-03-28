from django.urls import path
from . import views

app_name = 'todo'


urlpatterns = [
    path('',views.home,name='home'),
    path('create_todo/',views.create_todo,name='create_todo'),
]

