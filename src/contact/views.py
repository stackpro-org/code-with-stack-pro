from django.shortcuts import render, redirect

from .models import *
from header.models import *
from footer.models import *
#for CBV
from django.views import View
# for rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from . serializers import Contact_serializer

# class Contact_api(APIView):
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             name = request.data['name']
#             email = request.data['email']
#             subject = request.data['subject']
#             massage = request.data['massage']
#             contact = Contact()
#             contact.name = name
#             contact.email = email
#             contact.subject = subject
#             contact.message = massage
#             contact.save()
#             return Response({"success": "Contact has been sent"})



# class Contact_api(APIView):

#     def post(self, request, format=None):
#         serializer = Contact_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
        


class Contact_api(generics.CreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = Contact_serializer
        

# from . serializers import Contact_serializer

# class Contact_api(APIView):
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             name = request.data['name']
#             email = request.data['email']
#             subject = request.data['subject']
#             massage = request.data['massage']
#             contact = Contact()
#             contact.name = name
#             contact.email = email
#             contact.subject = subject
#             contact.message = massage
#             contact.save()
#             return Response({"success": "Contact has been sent"})



def contact(request):
    submitted = False
    template = 'contact.html'

    if request.method == 'POST':
        name = request.POST['name']  # this code works
        # name = request.POST.get('name')   ##this code works same thing like the above line
        # email = request.POST.get('email')
        email = request.POST['email']
        # subject = request.POST.get('subject')
        subject = request.POST['subject']
        # message = request.POST.get('message')
        message = request.POST['message']
        contact_data = Contact(name=name, email=email, subject=subject, message=message)
        contact_data.save()
        return redirect('/contact?submitted')

    else:
        if 'submitted' in request.GET:
            submitted = True
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_contact = Top_contact.objects.order_by()
    top_contact2 = Top_contact2.objects.order_by()
    top_contact3 = Top_contact3.objects.order_by()
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
        'top_contactdata': top_contact,
        'top_contactdata2': top_contact2,
        'top_contactdata3': top_contact3,
        'submitted': submitted,
    }

    return render(request, template_name=template, context=context)
