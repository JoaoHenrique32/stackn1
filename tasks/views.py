from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
   
def home(request):
    return HttpResponse("<h1>Bem-vindo ao meu site Django!</h1>")
 
