from django.urls import path
from . import views

app_name = 'todo'


urlpatterns = [
    path('',views.home,name='home'),
    path('create_todo/',views.create_todo,name='create_todo'),
    path('todo_details/<int:pk>/',views.todo_details,name='todo_details')
]

