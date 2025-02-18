from rest_framework.routers import DefaultRouter
from .api.viewsets import (
    UserViewSet,
    ProjectViewSet,
    TaskListViewSet,
    TaskViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'task_lists', TaskListViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls