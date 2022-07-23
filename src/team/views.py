from django.shortcuts import render
from .models import Team
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3
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
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
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

        

