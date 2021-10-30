from django.urls import path
from . import views

urlpatterns =[
    path('', views.index_login, name='index_login'),
    path('cadastrar/',views.cadastrar,name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sobreNos/', views.dashboard, name='sobre_nos'),
]