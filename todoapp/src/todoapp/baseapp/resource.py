# from import_export import resources
import resources

from .models import Task


class TaskResource(resources.ModelResource):
    class Meta:
        model = Task
