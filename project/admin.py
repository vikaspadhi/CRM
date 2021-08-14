from django.contrib import admin
from .models import *
from client.models import Client
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','client_link','type','status','assigned_to')
    list_editable = ('status',)
    search_fields = ['project_name','client']
    list_filter=('status','type')
    list_per_page = 25
    def client_link(self, project):
        url = reverse("admin:client_client_change", args=[project.client.id])
        link = '<a href="%s">%s</a>' % (url,project.client.name)
        return mark_safe(link)
    client_link.short_description = 'client'

    def get_queryset(self, request):
        project_list=super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name ='CTO').exists():
            self.readonly_fields=''
            return project_list
        if request.user.groups.filter(name ='Project Manager').exists():
            self.readonly_fields=('project_name','client','assigned_to','type','project_start_date','project_end_date','domain_detail','hosting_detail','domain_expiry_date','hosting_expiry_date','credentials','supporting')
            project_list = Project.objects.filter(assigned_to=request.user)
            return project_list


admin.site.register(Project,ProjectAdmin)