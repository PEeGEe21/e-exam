from django.db import models
from exam.models import Student
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.name} Profile'