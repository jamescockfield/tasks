from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.tasks.serializers.serializers import UserSerializer
from backend.tasks.models.models import User, Project, TaskList, Task

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]