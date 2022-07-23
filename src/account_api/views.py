from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class Account_api(APIView):
    '''
    POST request keys are user_name, email,  password,  confirm_password 
    '''
    def post(self, request, *args,**kwargs):
        if request.method == 'POST':
            username=request.data['user_name']
            email=request.data['email']
            password=request.data['password']
            confirm_password=request.data['confirm_password']
        
            if User.objects.filter(username=username).exists():
                return Response({"error": "An user already exists with this username!"})

            if User.objects.filter(email=email).exists():
                return Response({"error": "An user already exists with this email!"})

            if password != confirm_password:
                return Response({"error": " Password and Confirm Password not matched!"})
 
            user = User()
            user.username = username
            user.email = email
            user.password = password
            user.is_active = True
            user.set_password(raw_password=password) # this is valid hash password
            user.save()
            return Response({"success": "An user successfully creates an account"})


class Login_api(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
      
        if user is not None:
            login(request, user)
            return Response({"success":"Login successful"})
        else:
            return Response({"error":"username or password invalid"})



class Logout_api(APIView):
    def post(self, request):
        logout(request)

        return Response({"Logout successful"})


