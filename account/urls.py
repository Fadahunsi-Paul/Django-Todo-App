from django.urls import path
from . import views

app_name = 'accounts' 

urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('login_view/',views.login_view,name='login'),
    path('logout_view/',views.logout_view,name='logout'),
]
