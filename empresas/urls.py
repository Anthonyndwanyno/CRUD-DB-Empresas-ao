from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    #path('login/', views.login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),
    path('empresa_record/<int:pk>', views.empresa_record, name="empresa_record"),
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
    path('add_record/', views.add_record, name="add_record"),
    path('update_record/<int:pk>', views.update_record, name="update_record"),
] 