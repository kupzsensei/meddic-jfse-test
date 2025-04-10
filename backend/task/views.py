from django.shortcuts import render
from rest_framework import generics
from .models import Task, Category
from .serializers import CategorySerializer , TaskReadSerializer, TaskWriteSerializer , TaskRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters

# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().select_related('user')
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Category '{instance.name}' deleted successfully."},
            status=status.HTTP_200_OK
        )
    

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('category')
    serializer_class = TaskReadSerializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['completed', 'priority']
    search_fields = ['name', 'description' , 'category__name' , 'subtasks__name']
    ordering_fields = ['name', 'id', 'due_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskWriteSerializer
        return super().get_serializer_class()

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('category').prefetch_related('subtasks')
    serializer_class = TaskRetrieveSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskWriteSerializer
        return super().get_serializer_class()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Task '{instance.name}' deleted successfully."},
            status=status.HTTP_200_OK
        )