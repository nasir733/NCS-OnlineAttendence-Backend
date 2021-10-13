from django.db import models
from django.contrib.auth import get_user_model  # Create your models here.
from django.contrib.postgres.fields import ArrayField
from ndarray import NDArrayField

User = get_user_model()
class Attendence(models.Model):
    """
    Attendence model
    """
    year = models.IntegerField()
    month = models.IntegerField()
    day= models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    presentStudents = models.ManyToManyField(User,related_name='presentStudents',related_query_name='presentStudents')
    
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

class FaceEncoding(models.Model):
    """
    FaceEncoding model
    """
    encodings = ArrayField(
        ArrayField(
          models.FloatField(null=True, blank=True),
        ),null=True, blank=True
    )
    classNames = ArrayField(
        ArrayField(
          models.CharField(null=True,blank=True,max_length=999),
        ),null=True, blank=True
    )
