from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

# Create your views here.
@api_view(['POST'])
def user_signup(request):
    print("this is a user_signup function")
    try:
        first_name = request.data['first_name']




    except Exception as e:
        print(e)


