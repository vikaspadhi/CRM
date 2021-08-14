from django.db import models
from financial.models import Receipt
from django.contrib import admin
from .models import *
from client.models import Client
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponse
from django.conf.urls import url
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Register your models here.

class ReceiptAdmin(admin.ModelAdmin):
    readonly_fields = ('download_link',)
    feilds=('client','date','description','amount','download_link')
    list_display=['client','date','download_link',]



    def get_queryset(self, request):
        receipt_list=super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name ='CTO').exists():
            return receipt_list
        if request.user.groups.filter(name ='Project Manager').exists():
            project_list = Project.objects.filter(assigned_to=request.user)
            project_names=project_list.values('project_name')
            pnames=[]
            for i in range(len(project_names)):
                pnames.append(project_names[i]['project_name'])
            receipt_list=Receipt.objects.filter(project__in=pnames)
            return receipt_list
    
    # add custom view to urls
    def get_urls(self):
        urls = super(ReceiptAdmin, self).get_urls()
        urls += [
            url(r'^download-file/(?P<pk>\d+)$',self.download_file,name='financial_Receipt_download-file'),
        ]
        return urls

    # custom "field" that returns a link to the custom function
    def download_link(self, obj):
        print(obj)
        return format_html(
            '<a href="{}">Click here</a>',reverse('admin:financial_Receipt_download-file', args=[obj.pk])
        )
    download_link.short_description = "View Receipt"

    
    # add custom view function that downloads the file
    def download_file(self, request, pk=None):
        template_path = 'financial/receipt.html'
        receipt_obj=Receipt.objects.filter(id=pk)
        receipt_detail=receipt_obj.values()[0]

        client_email=receipt_detail['client_id']
        project_id=receipt_detail['project_id']

        client_obj=Client.objects.filter(email=client_email)
        client_detail=client_obj.values()[0]

        project_obj=Project.objects.filter(project_name=project_id)
        project_detail=project_obj.values()[0]

        def Merge(dict1, dict2,dict3):
            res = dict1 | dict2 | dict3
            return res

        receipt = Merge(receipt_detail,client_detail,project_detail)
        context = receipt
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="receipt.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors')
        return response
    
admin.site.register(Receipt,ReceiptAdmin)