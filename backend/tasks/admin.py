from django.contrib import admin
from .models.models import UserProfile, Project, TaskList, Task

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    search_fields = ('user__username',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'order')
    list_filter = ('project',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to', 'due_date')
    search_fields = ('title', 'description')
    list_filter = ('status', 'due_date')
