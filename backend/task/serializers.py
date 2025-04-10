from rest_framework import serializers
from .models import Task, Category, SubTask , FileUpload

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubTaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'name', 'completed']

class SubTaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['name', 'completed']

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['id', 'file', 'uploaded_at']

    def validate_file(self, value):
        if value.size > 20 * 1024 * 1024:
            raise serializers.ValidationError("File too large. Maximum size is 20MB.")
        # uncomment this to restrict file types
        # if not value.name.endswith(('.pdf', '.docx', '.png')):
        #     raise serializers.ValidationError("Unsupported file type.")
        return value

class TaskReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'category', 'completed_date', 'due_date', 'completed', 'priority']



class TaskWriteSerializer(serializers.ModelSerializer):
    subtasks = SubTaskWriteSerializer(many=True, required=False)
    files = FileUploadSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'category', 'completed_date', 'due_date', 'completed', 'priority' , 'subtasks', 'files']
    
    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        files_data = validated_data.pop('files', [])
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)
        for file_data in files_data:
            FileUpload.objects.create(task=task, **file_data)
        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks',[])
        files_data = validated_data.pop('files', [])
        instance.subtasks.all().delete()  # Delete existing subtasks
        for subtask in subtasks_data:
            SubTask.objects.create(task=instance, **subtask)
        instance.files.all().delete()
        for file in files_data:
            FileUpload.objects.create(task=instance, **file)

        # Update other fields on the task instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TaskRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subtasks = SubTaskReadSerializer(many=True, read_only=True)
    files = FileUploadSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'category', 'completed_date', 'due_date', 'completed', 'priority', 'subtasks' , 'files']

    