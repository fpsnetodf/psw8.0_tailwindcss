from django.urls import path
from . import views
urlpatterns = [    
    path('', views.home, name="home"), 
    path("novo/", views.novo, name='novo'),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
]