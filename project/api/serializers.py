from rest_framework import serializers
from .models import Student

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
class Stu_serializers(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=["id","stu_name","stu_email","stu_contat","stu_city"]
