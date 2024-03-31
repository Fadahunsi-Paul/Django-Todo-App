from django.urls import path
from . import views

app_name = 'todo'


urlpatterns = [
    path('',views.home,name='home'),
    path('create_todo/',views.create_todo,name='create_todo'),
    path('todo_details/<int:pk>/',views.todo_details,name='todo_details'),
    path('todo_update/<int:pk>/',views.update_todo,name='todo_update'),
    path('todo_delete/<int:pk>/',views.delete_todo,name='todo_delete'),
]

