from django.contrib import admin
from .models import LGNode, Task


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
        return False

admin.site.register(Task)