from django.db import models
from django.contrib.auth import get_user_model  # Create your models here.
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
