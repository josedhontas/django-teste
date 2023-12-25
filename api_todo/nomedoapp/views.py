from nomedoapp.models import Todo
from nomedoapp.serializers import TodoSerializer
from rest_framework import viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
 