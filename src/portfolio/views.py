from django.shortcuts import render, redirect, get_object_or_404
from header.models import Top_header, Header
from .models import *
from rest_framework import generics
from.serializers import Portfolio_serializer
from rest_framework.response import Response
from rest_framework.views import APIView

def portfolio(request):
    template = 'portfolio.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()

    all_cat = Category.objects.all()
    cat = request.GET.get('categ')

    if cat == None:

        portfolio = Portfolio.objects.all()

    else:
        portfolio = Portfolio.objects.filter(catagory__name=cat)

    context = {
        'top_headerdata': top_header,
        'headerdata': header,
     
        'portfolio': portfolio,
        'category': all_cat,

    }
    return render(request, template_name=template, context=context)

class Portfolio_class(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_serializer
    

        


def details(request, slug):

    template = 'portfolio-details.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    portfolio = Portfolio.objects.all()
    post = get_object_or_404(portfolio, slug=slug)

    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'post': post,
    }

    return render(request, template_name=template, context=context)


