from rest_framework import serializers
from .models import Person, Company




class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= ['company_name']

class PeopleSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    # with_code = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields= "__all__"
        depth = 1

    # def get_with_code(self,obj):
    #     company_obj = Company.objects.get(id=obj.company.id)
    #     return {'company_obj':company_obj.company_name,'company_code':"112"}
    
    def validate(self,data):

        if any([a in "!@#$%^&*()_+{}[];:<>" for a in data['name']]):
            raise serializers.ValidationError("name is invalid")
        if data['age'] <= 1:
            raise serializers.ValidationError("age is invalid")
        
        return data
