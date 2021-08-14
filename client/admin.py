from django.contrib import admin
from .models import *
from project.models import Project
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone_number1')
    # list_editable = ('verified',)
    search_fields = ['name','email']
    # readonly_fields=('slug',)
    list_per_page = 10


    def get_queryset(self, request):
        client_list=super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name ='CTO').exists():
            return client_list
        if request.user.groups.filter(name ='Project Manager').exists():
            project_list = Project.objects.filter(assigned_to=request.user)
            clist=project_list.values('client')
            client_email=[]
            for i in range(len(clist)):
                client_email.append(clist[i]['client'])
            client_list=Client.objects.filter(email__in=client_email)
            return client_list

admin.site.register(Client,ClientAdmin)