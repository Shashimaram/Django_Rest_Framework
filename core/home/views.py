from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



@api_view(['GET','POST'])
def index(request):
    courses = {
        'course_name': 'Python',
        "learn" : ['flase', 'django','tornado','fastApi'],
        'course_provider': "Scaler",
    }
    if request.method == 'GET':
        print("you hit a get method")
        return Response(courses)
    elif request.method == 'POST':
        print("you hit a Post method")
        return Response()
