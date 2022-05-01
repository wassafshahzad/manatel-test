from pyexpat import model
from rest_framework import serializers
from .models import SchoolModel, StudentModel



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = "__all__"

    def update(self, instance, validated_data):

        # Dont update total students if the number is decreasing
        if instance.total_students > validated_data["total_students"]:
            validated_data.pop("total_students") 
        return super().update(instance, validated_data)



class StudentSerializer(serializers.ModelSerializer):
    school  = serializers.SlugRelatedField(slug_field="name", many=False, 
        queryset=SchoolModel.objects.all())
    
    class Meta:
        model = StudentModel
        fields = "__all__"
        read_only_fields = ['id_string']
