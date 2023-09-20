from rest_framework import serializers
from .models import Task, Tag

class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all(), allow_empty=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'tags']

    def validate(self, attrs):
        due_date = attrs.get('due_date')
        timestamp_created = self.instance.timestamp if self.instance else None

        if due_date and timestamp_created and timestamp_created > due_date:
            raise serializers.ValidationError("Due Date cannot be before the Timestamp created.")

        return attrs

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:
            tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tags_data]
            instance.tags.set(tags)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        task = Task.objects.create(**validated_data)
        if tags_data:
            tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tags_data]
            task.tags.set(tags)
        return task
