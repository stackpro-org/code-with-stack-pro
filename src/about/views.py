from django.shortcuts import render
from . models import Count, Testimonial2, Testimonial1, Client, About, Client_image
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3


def about_page(request):
    template = 'about.html'


    count = Count.objects.order_by()
    testi2 = Testimonial2.objects.order_by()
    testi1 = Testimonial1.objects.order_by()
    about = About.objects.order_by()
    client = Client.objects.order_by()
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    context = {

        'countdata': count,
        'testdata1': testi1,
        'testdata2': testi2,
        'clientdata': client,
        'aboutdata': about,
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
        

    }

    return render(request, template_name=template, context=context)

