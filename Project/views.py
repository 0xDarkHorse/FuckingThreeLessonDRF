from rest_framework.viewsets import ModelViewSet
from .models import Projects, TODO
from main.models import Users
from .serializers import ProjectsModelSerializer, TODOModelSerializer


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
