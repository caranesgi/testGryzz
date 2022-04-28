from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerApp, name="register"),
    path('login', views.loginApp, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),


    path('', views.home, name="home"),
    path('empresas', views.empresa, name="empresas"),
    path('administradores/<str:pk>/', views.admnistrador, name="administradores"),
    path('sedes', views.sede, name="sedes"),

    path('crear_empresa/', views.crearEmpresa, name="crear_empresa"),
    path('actualizar_empresa/<str:pk>/', views.actualizarEmpresa, name="actualizar_empresa"),
    path('eliminar_empresa/<str:pk>/', views.eliminarEmpresa, name="eliminar_empresa"),

    path('crear_administrador/', views.crearAdministrador, name="crear_administrador"),
    #path('actualizar_administrador/<str:pk>/', views.actualizarAdministrador, name="actualizar_administrador"),
    path('eliminar_administrador/<str:pk>/', views.eliminarAdministrador, name="eliminar_administrador"),

    path('crear_admin_empresa/', views.registarAdminEmpresa, name="registrar_adminEmpresa"),


]