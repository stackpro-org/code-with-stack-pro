from django.shortcuts import render
from .models import Hero, Featured
from about.models import About, Client
from services.models import Service
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3


def index(request):
    hero = Hero.objects.order_by()
    feature = Featured.objects.order_by()
    about = About.objects.order_by()
    client = Client.objects.order_by()
    service = Service.objects.order_by()
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()

    context = {
        'herodata': hero,
        'featuredata': feature,
        'aboutdata': about,
        'clientdata': client,
        'servicedata': service,
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
    }
    template = 'index.html'
    return render(request, template_name=template, context=context)







