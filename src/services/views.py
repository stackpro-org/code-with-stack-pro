from django.shortcuts import render
from . models import Service, Skill
from header.models import Top_header, Header

from rest_framework.views import APIView
from rest_framework.response import Response

def services(request):
    service = Service.objects.order_by()
    skill = Skill.objects.order_by()
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
 
    context = {
        'servicedata' : service,
        'skilldata' : skill,
        'top_headerdata' : top_header,
        'headerdata' : header,

    }
    template = 'services.html'
    return render(request, template_name=template, context=context)

