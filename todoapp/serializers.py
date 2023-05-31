from rest_framework import serializers
from .models import Task, Tag

class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all(), allow_empty=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'tags']

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:
            tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tags_data]
            instance.tags.set(tags)
        return super().update(instance, validated_data)
