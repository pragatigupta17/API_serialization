from rest_framework import serializers

class Stu_serializers(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    stu_name=serializers.CharField(max_length=50)
    stu_email=serializers.EmailField()
    stu_contat=serializers.IntegerField()
    stu_city=serializers.CharField(max_length=50)