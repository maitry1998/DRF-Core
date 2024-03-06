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


@api_view(['GET','POST','PUT','PATCH'])
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
    
    #update to databse , in here, you also pass the object
    elif request.method =="PUT":
        serializer = PeopleSerializer(Person.objects.get(id=request.data['id']),data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    #update to databse , in here, you also pass the object difference with PUT is that partial update is allowed
    elif request.method =="PATCH":
        serializer = PeopleSerializer(Person.objects.get(id=request.data['id']),partial=True,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    

