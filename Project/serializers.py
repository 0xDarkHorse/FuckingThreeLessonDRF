from rest_framework import serializers
from .models import Projects, TODO
from main.models import Users


class ProjectsModelSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Users.objects.all())
    url_git = serializers.URLField(required=False)

    class Meta:
        model = Projects
        fields = '__all__'


class TODOModelSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all()) # Fuck, Not use all()..

    class Meta:
        model = TODO
        exclude = ('data_create', 'data_edit')
