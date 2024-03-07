from django.shortcuts import render
from .models import Person
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from home.serializers import PeopleSerializer
from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

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


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    #serializing -> from queryset to json
    if request.method =="GET":
        
        serializer = PeopleSerializer(Person.objects.filter(company__isnull=False),many=True)
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
    # no need of serializer here
    elif request.method =="DELETE":
        Person.objects.get(id=request.data['id']).delete()
        return Response({"message":"id deleted"})


################################
#   CBV
################################  
    
from rest_framework.views import APIView


class PersonAPI(APIView):

    def get(self,request):
        serializer = PeopleSerializer(Person.objects.filter(company__isnull=False),many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PeopleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request):
        serializer = PeopleSerializer(Person.objects.get(id=request.data['id']),data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request):
        serializer = PeopleSerializer(Person.objects.get(id=request.data['id']),partial=True,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request):
        Person.objects.get(id=request.data['id']).delete()
        return Response({"message":"id deleted"})

################################
#   Model Viewset
################################  

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
class PeopleViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self,request):
        queryset=self.queryset
        if request.GET.get('search'):
            queryset= self.queryset.filter(name__startswith=request.GET.get('search'))

        searielizer= PeopleSerializer(queryset,many=True)
        return Response(searielizer.data)
