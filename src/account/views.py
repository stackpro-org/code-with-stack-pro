from multiprocessing.spawn import import_main_path
from django.shortcuts import render, redirect
from header.models import Top_header, Header
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from . forms import ProfileForm
from django.core.mail import send_mail
from django.conf import settings
from team.pdf import html_to_pdf
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View
from account.models import Account

def account(request):

    if request.method == 'POST':
        uname = request.POST.get('user_name')
        email = request.POST.get('email')
        psd = request.POST.get('password')
        cpsd = request.POST.get('confirm_password')
        if psd == cpsd:
            if Account.objects.filter(username=uname).exists():

                messages.error(request, 'Username already exists!')
                return redirect('account')

            elif Account.objects.filter(email=email).exists():

                messages.error(request, 'The Email already exists!')
                return redirect('account')

            else:

                user = Account.objects.create_user(
                    username=uname, email=email, password=psd)

                user.save()
                messages.success(request, 'Account has been created successfully')
             
                return redirect('login')

        else:
            messages.error(request, 'Password and confirm-password not matched!')
            return redirect('account')

    template = 'account/account.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    
    context = {
        'top_headerdata': top_header,
        'headerdata': header,

    }

    return render(request, template_name=template, context=context)




# def verify(request):
#     template = 'account/verify.html'
#     if request.method == 'POST':
#         code = request.POST.get('code')
#         profile = Profile.objects.filter(auth_token=code).first()
#         if profile:
#             if profile.is_verified:
#                 messages.success(request, 'Your account already verified')
#                 return redirect('login')
#             profile.is_verified = True
#             profile.save()
#             messages.success(request, 'Your account is verified')
#             return redirect('login')
#         else:
#             messages.error(request, 'Not matched the code check your email')







#     return render(request, template_name=template)



def authlogin(request):
    template = 'account/login.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()


    context = {
        'top_headerdata': top_header,
        'headerdata': header,


    }

    if request.method == 'POST':
        email = request.POST.get('email')
        pas = request.POST.get('password')
        user = authenticate(request, email=email, password=pas)
    
               
        if user is not None:
            login(request, user)

            return redirect('index')
        else:
            messages.error(request, 'Invalid password or Email')


    return render(request, template_name=template, context=context)


# def forget(request):
#     template = 'account/forget.html'
#     top_header = Top_header.objects.order_by()
#     header = Header.objects.order_by()
#     top_footer1 = Top_footer1.objects.order_by()
#     top_footer2 = Top_footer2.objects.order_by()
#     top_footer3 = Top_footer3.objects.order_by()
#     top_footer4 = Top_footer4.objects.order_by()
#     context = {
#         'top_headerdata': top_header,
#         'headerdata': header,
#         'footer1': top_footer1,
#         'footer2': top_footer2,
#         'footer3': top_footer3,
#         'footer4': top_footer4,
#     }
#     return render(request, template_name=template, context=context)
# from django.forms.models import model_to_dict
# import json


def profile(request):
    template = 'account/profile.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
   
    profile = request.user
   

    

    context = {
                'top_headerdata': top_header,
             'headerdata': header,
 
             'profile': profile,
            
             
       }


    return render(request, template_name=template, context=context)

def user_profile(request, pk):
    template = 'account/profile.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
 
    profile = Account.objects.get(id=pk)

   

    context = {
                'top_headerdata': top_header,
             'headerdata': header,

             'profile': profile,
            
             
       }


    return render(request, template_name=template, context=context)

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        profile = request.user 

     
      

        context = {
               'profile': profile,
              
           }
        pdf = html_to_pdf('pdf.html', context)
             # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')






def update_profile(request):

    template = 'account/update_profile.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()


    if request.method == "POST":
        profile = request.user
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        pform.save()
        return redirect('profile')
    else:
        # here user father and profile is son it happens when user is used with OneToOneFiedls
        profile = request.user

        pform = ProfileForm(instance=profile)

    context = {
        'form': pform,
        'top_headerdata': top_header,
        'headerdata': header,
    
    }
    return render(request, template_name=template, context=context)


def userlogout(request):
    logout(request)
    return redirect('login')


# def sent_registation_mail(email, token, username):
#     subject = 'Your accounts need to be verified'
#     message = f'Hi {username}! welcome to Stack Pro. Here is the verification CODE  {token}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, email_from, recipient_list)