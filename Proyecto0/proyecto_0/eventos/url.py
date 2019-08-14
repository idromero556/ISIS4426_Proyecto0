from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/registro/', views.agregarUsuarioview, name="agregarUsuario"),
    path('registroUsuario/', views.agregarUsuario, name = "registroUsuario"),
    path('agregarEvento/', views.agregarEvento, name = "agregarEvento"),
    path('agregarNuevoEvento/', views.agregarNuevoEvento, name="agregarNuevoEvento"),
    path('login/', views.login_view, name='login'),
    path('loginUser/', views.login_user, name='loginUser'),
    path('logout/', views.logout_view, name='logout'),
    path('isLogged/', views.is_logged_view, name='isLogged'),
    url(r'^verDetalle/(?P<pk>\d+)/$', views.verDetalle, name='verDetalle'),
    url(r'^verDetalle/(?P<pk>\d+)/eliminarEvento$', views.eliminarEvento, name='eliminarEvento'),
    url(r'^verDetalle/(?P<pk>\d+)/editarEvento1', views.editarEventoView, name='editarEvento1'),
    url(r'^verDetalle/(?P<pk>\d+)/editarEvento', views.editarEvento, name='editarEvento'),
]

