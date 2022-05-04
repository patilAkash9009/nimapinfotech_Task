from .models import Project,Client
from rest_framework import serializers

class ProjectSerializer (serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','project_name']


class ClientSerializer (serializers.ModelSerializer):
    Projects = ProjectSerializer(read_only=True, many=True)
    created_by = serializers.SlugRelatedField(slug_field='username',read_only = True)
    class Meta:
        model = Client
        fields = ['id','client_name','Projects','created_at','created_by','updated_at']