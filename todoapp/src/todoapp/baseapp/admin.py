from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import Task, Book
from .resource import TaskResource


# from import_export.admin import ImportExportModelAdmin


# admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'priority', 'status', 'created', 'is_deleted')
    list_display = ('id', 'name', 'priority', 'status', 'created')


admin.site.register(Task, TaskAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'price')


admin.site.register(Book, BookAdmin)

# class TaskAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name', 'priority', 'status', 'created')
#     resource_class = TaskResource
#
#
# admin.site.register(Task, TaskAdmin)
