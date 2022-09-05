from django.urls import path

from apponline import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('carteras/', views.carteras, name="carteras"),
    path('camperas/', views.camperas, name="camperas"),
    path('zapatos/', views.zapatos, name="zapatos"),
    path('accesorios/', views.accesorios, name="accesorios"),
    path('crear-carteras/', views.carteras_formulario, name="carteras_formulario"),
    path('busqueda-carteras-form/', views.busqueda_carteras, name="busqueda_carteras_form"),
    path('busqueda-carteras/', views.buscar, name="busqueda_carteras"),
]
