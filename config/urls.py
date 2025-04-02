"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from tasks.urls import router as tasks_router
from users.urls import urlpatterns as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(tasks_router.urls)),  # Tarefas
    path('api/auth/', include(users_urls)),  # Autenticação JWT
    path('', include('tasks.urls')),  # Direciona a home para o app 'tasks'
    path('users/', include('users.urls')),  # Se precisar de rotas para 'users
]
