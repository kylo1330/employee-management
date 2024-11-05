from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required



def home(request):
    
    return render(request,'index.html')

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)





#    api worked in postman 


# from django.views.decorators.csrf import csrf_exempt 
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny,IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK
# from rest_framework.permissions import BasePermission
# from rest_framework import status
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from rest_framework.authtoken.models import Token
# from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


# class IsSuperUser(BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.is_superuser


# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def signup(request):
#     form = UserCreationForm(data=request.data)
#     if form.is_valid():
#         user = form.save()
#         return Response({"success": True, "message": "Account created successfully."}, status=status.HTTP_201_CREATED)
    
#     errors = form.errors.as_json() 
#     return Response({"success": False, "errors": errors}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    
#     try:
#         user = User.objects.get(username=username)
#         if user.check_password(password):
#             token, _ = Token.objects.get_or_create(user=user)
#             is_superuser = user.is_superuser
#             return Response({'token': token.key, 'is_superuser': is_superuser}, status=HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid Credentials'}, status=HTTP_400_BAD_REQUEST)
#     except User.DoesNotExist:
#         return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)


# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def logout(request):
#     response = Response({'message': 'Logout successful'}, status=HTTP_200_OK)
#     response.delete_cookie('token')  
#     return response     