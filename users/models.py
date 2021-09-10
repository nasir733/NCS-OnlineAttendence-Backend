from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField
class UserAccountManager(BaseUserManager):
    def create_user(self, email,first_name,last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name ,last_name=last_name)

        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_thumbnail = ImageSpecField(source='profile_pic',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    

    address= models.TextField(max_length=555, blank=True,null=True)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_student=models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    GRADE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('TEACHER','Teacher'),
        ('WORKER','Worker')
        
    )

    grade = models.CharField(max_length=9,
                             choices=GRADE_CHOICES,
                             default="1")
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
