from .utils import generate_unique
from django.db import models



class SchoolModel(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    total_students = models.IntegerField()


class StudentModel(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=20)
    last_name = models.CharField(null=False, blank=False, max_length=20)
    # This can be the primarykey for this model however I like to have
    id_string = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(SchoolModel, related_name="students", 
        null=False, blank=False, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.id_string =  generate_unique(20)
        super().save(*args, **kwargs)

