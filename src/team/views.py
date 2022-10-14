from django.shortcuts import render
from .models import Team
from header.models import Top_header, Header
from . serializers import Team_serializer
from rest_framework.response import Response
from xhtml2pdf import pisa
from django.http import HttpResponse
from rest_framework.views import APIView

from django.views.generic import View
from .pdf import html_to_pdf 




def team(request):
    template = 'team.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    team = Team.objects.order_by()
    
    context = {
        'top_headerdata': top_header,
        'headerdata': header,

        'teamdata': team,
    }
    return render(request, template_name=template, context=context)




#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        # getting the template
        team = Team.objects.order_by()
     
        context = {
            'teamdata': team,
        }
        pdf = html_to_pdf('pdf.html', context)

         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')






class Team_api(APIView):

    def get(self,request, format=None):
        team = Team.objects.all()
        team_serialized = Team_serializer(team, many=True)
        return Response(team_serialized.data)

        

