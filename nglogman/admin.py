from django.contrib import admin
from .models import LGNode, Task, NodeGroup


# Register your models here.
@admin.register(LGNode)
class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []
    change_form_template = "admin/admin_readonly.html"

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    scheduler = None
    job = None

    def save_model(self, request, obj, form, change):
        from nglm_grpc.gRPCMethods import scheduleTask
        self.scheduler, self.job = scheduleTask(obj)
        print('scheduleTask called')
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if self.job is not None:
            self.job.remove()
            print('job with id %s removed.' % self.job.id)
        super().delete_model(request, obj)


admin.site.register(NodeGroup)
