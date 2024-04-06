from rest_framework.routers import DefaultRouter

from apps.base.views import TaskApiView

router = DefaultRouter()
router.register('tasks', TaskApiView, "api_tasks")

urlpatterns = router.urls