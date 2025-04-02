from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path
from .views import home

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('', home, name='home'),  # Rota para a página inicial
]

