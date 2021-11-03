"""disney_liverano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('nido/servizi/', views.nido_servizi, name='nido_servizi'),
    path('nido/regolamento/', views.nido_regolamento, name='nido_regolamento'),
    path('primavera/servizi/', views.primavera_servizi, name='primavera_servizi'),
    path('primavera/regolamento/', views.primavera_regolamento, name='primavera_regolamento'),
    path('infanzia/ptof/', views.ptof, name='ptof'),
    path('infanzia/documentazione/', views.documentazione, name='documentazione'),
]
