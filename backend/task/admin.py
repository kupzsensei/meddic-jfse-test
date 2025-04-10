from django.contrib import admin
from .models import Task, Category , FileUpload , SubTask

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(FileUpload)
admin.site.register(SubTask)