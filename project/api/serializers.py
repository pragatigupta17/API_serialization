from rest_framework import serializers
from .models import Student
from .models import Employ
from .models import Client
from .models import Teacher
from .models import School

"""class Stu_serializers(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    stu_name=serializers.CharField(max_length=50)
    stu_email=serializers.EmailField()
    stu_contat=serializers.IntegerField()
    stu_city=serializers.CharField(max_length=50)

    def create(self, validated_data):
        
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
        instance.stu_name = validated_data.get('stu_name', instance.stu_name)
        instance.stu_email = validated_data.get('stu_email', instance.stu_email)
        instance.stu_contact = validated_data.get('stu_contact', instance.stu_contact)
        instance.stu_city = validated_data.get('stu_city', instance.stu_city)
       
        instance.save()
        return instance"""

'''class Stu_serializers(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=["id","stu_name","stu_email","stu_contat","stu_city"]'''
#----------------------------------------------------------------------------------------------

class Pragati_serializers(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=["id","stu_name","stu_email","stu_contat","stu_city"]
class Sajal_serializers(serializers.ModelSerializer):
    class Meta:
        model= Employ
        fields=["id","emp_name","emp_email","emp_contat","emp_city"]
class Prabha_serializers(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields=["id","cnt_name","cnt_email","cnt_contat","cnt_city"]
class Neeraj_serializers(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields=["id","tch_name","tch_email","tch_contat","tch_city"]
class Aditi_serializers(serializers.ModelSerializer):
    class Meta:
        model= School
        fields=["id","sch_name","sch_email","sch_contat","sch_city"]
