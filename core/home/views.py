from django.shortcuts import render
from .models import Person
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from home.serializers import PeopleSerializer
@api_view(['GET','POST'])
def index(request):
    if request.method =="GET":
        print(request.GET.get("search"))
        courses={
            "coursename": "python",
            "learn":["flask","django","fastAPI"],
            "course_provider":"FSU"
        }
    elif request.method =="POST":
        print("\n\n\n")
        print(request.data)
        courses = {"data":"Post data"}
    elif request.method =="PUT":
        courses = {"data":"Put data"}

    return Response(courses)


@api_view(['GET','POST'])
def person(request):
    #serializing -> from queryset to json
    if request.method =="GET":
        
        serializer = PeopleSerializer(Person.objects.all(),many=True)
        return Response(serializer.data)
    
    #Deserializer -> from json to queryset
    elif request.method =="POST":
        serializer = PeopleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    

