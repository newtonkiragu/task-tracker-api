from rest_framework.routers import DefaultRouter

from api.views import TasksViewSet

router = DefaultRouter()

router.register(r'tasks', TasksViewSet, basename='tasks')
urlpatterns = router.urls
