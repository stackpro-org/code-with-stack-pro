from django.shortcuts import render
from . models import Service, Skill
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3
from rest_framework.views import APIView
from rest_framework.response import Response

def services(request):
    service = Service.objects.order_by()
    skill = Skill.objects.order_by()
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    context = {
        'servicedata' : service,
        'skilldata' : skill,
        'top_headerdata' : top_header,
        'headerdata' : header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
    }
    template = 'services.html'
    return render(request, template_name=template, context=context)

