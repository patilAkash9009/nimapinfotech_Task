from django.contrib import admin
from .models import Project,Client
# Register your models here.

class ProjectAdmin (admin.ModelAdmin):
    list_display = ['id','project_name']
admin.site.register(Project,ProjectAdmin)


class ClientAdmin (admin.ModelAdmin):
    list_display = ['id','client_name','created_at','created_by','updated_at']
admin.site.register(Client,ClientAdmin)