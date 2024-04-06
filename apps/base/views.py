from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.base.models import Task
from apps.base.serializers import TaskSerializers
class TaskApiView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    