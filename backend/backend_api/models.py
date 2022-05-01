from rest_framework.exceptions import ValidationError
from .utils import generate_unique
from django.db import models



class SchoolModel(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20, unique=True)
    total_students = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

class StudentModel(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=20)
    last_name = models.CharField(null=False, blank=False, max_length=20)
    # This can be the primarykey for this model however I like to have the
    # Default primary key of django
    id_string = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(SchoolModel, related_name="students", 
        null=False, blank=False, on_delete=models.CASCADE)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    
    def _get_id_string(self) -> str:
        return generate_unique(20) if not self.id_string else self.id_string

    def save(self, *args, **kwargs):
        self.id_string =  self._get_id_string()
        if self.school.total_students == self.school.students.count():
            raise ValidationError("Student limit reached")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.full_name