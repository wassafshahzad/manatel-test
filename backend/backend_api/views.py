from rest_framework import viewsets
from .models import SchoolModel, StudentModel
from .serializers import SchoolSerializer, StudentSerializer


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer