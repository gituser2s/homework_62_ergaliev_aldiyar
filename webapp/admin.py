from django.contrib import admin
from webapp.models import Task, Type, Status, Project, User

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'detailed_description', 'status', 'project', 'created_at')
    list_filter = ('id', 'description', 'detailed_description', 'status', 'type', 'project', 'created_at')
    search_fields = ('description', 'detailed_description', 'status', 'type', 'project',)
    fields = ('description', 'detailed_description', 'status', 'type', 'project', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')


admin.site.register(Task, TaskAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title',)
    fields = ('title',)
    readonly_fields = ('id',)


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title',)
    fields = ('title',)
    readonly_fields = ('id',)


admin.site.register(Status, StatusAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'start_date', 'end_date')
    list_filter = ('id', 'title', 'start_date', 'end_date')
    search_fields = ('title', 'start_date', 'end_date')
    fields = ('title', 'start_date', 'end_date')
    readonly_fields = ('id',)


admin.site.register(Project, ProjectAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project')
    list_filter = ('id', 'user', 'project')
    search_fields = ('user', 'project')
    fields = ('user', 'project')
    readonly_fields = ('id',)


admin.site.register(User, UserAdmin)