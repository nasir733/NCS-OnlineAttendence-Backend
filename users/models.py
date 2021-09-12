from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import os 
from phonenumber_field.modelfields import PhoneNumberField
import datetime
import sys
from PIL import Image
from io import BytesIO
from django.core.files import File
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class UserAccountManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,profile_pic,roll_no,grade,phone_number=None,address=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name ,last_name=last_name,profile_pic=profile_pic,roll_no=roll_no,grade=grade,phone_number=phone_number,address=address)

        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, first_name, last_name, password,profile_pic,roll_no,grade,phone_number=None,address=None):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, profile_pic=profile_pic,
                                roll_no=roll_no, grade=grade, phone_number=phone_number, address=address,password=password)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user



def wrapper(instance, filename):
    ext = filename.split('.')[-1]
            # get filename

    filename = '{}{}'.format(instance.first_name, instance.last_name)
    filename=f'{instance.first_name}-{instance.last_name}-{instance.roll_no}.{ext}'

    return os.path.join('profile_pic', filename)


def last_matched_wrapper(instance, filename):
    ext = filename.split('.')[-1]
    # get filename

    filename = '{}{}'.format(instance.first_name, instance.last_name)
    filename = f'{instance.first_name}-{instance.last_name}-{instance.roll_no}-{datetime.time}.{ext}'

    return os.path.join('last_matched_image', filename)
    
class UserAccount(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    profile_pic = ProcessedImageField(
        upload_to=wrapper, blank=True,
        format='PNG',
        options={'quality': 100})
    roll_no = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_matched_image = ProcessedImageField(
        upload_to=last_matched_wrapper, blank=True,
        format='PNG',
        options={'quality': 100},null=True)

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
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'profile_pic', 'roll_no', 'grade', 'phone_number', 'address']


    def compressImage(self, image):
        img = Image.open(image).convert("RGB")
        im_io = BytesIO()
        img.save(im_io, format='jpeg', optimize=True, quality=55)
        new_image = File(im_io, name="%s.jpeg" % image.name.split('.')[0],)
        return new_image
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class last_detected_images (models.Model):

    file = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(
        "UserAccount", related_name="photos", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "last_detected_image"
        verbose_name_plural = "last_detected_images"

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

