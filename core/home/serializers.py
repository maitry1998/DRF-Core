from rest_framework import serializers
from .models import Person
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields= "__all__"

    def validate(self,data):

        if any([a in "!@#$%^&*()_+{}[];:<>" for a in data['name']]):
            raise serializers.ValidationError("name is invalid")
        if data['age'] <= 1:
            raise serializers.ValidationError("age is invalid")
        
        return data
