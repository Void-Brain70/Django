from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    Picture_Picture = models.ImageField(upload_to='Images/profile')
    Phone = models.IntegerField(null=True,blank=True)


    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username