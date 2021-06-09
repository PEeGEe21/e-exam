from django.db import models
from exam.models import Teacher
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    coverimage = models.ImageField(default='default.png', upload_to='cover_pics')

    def __str__(self):
        return f'{self.user.name} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)