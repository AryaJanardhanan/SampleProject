from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='gallery/',default=0)
    doc = models.FileField(upload_to='documents/',default=0)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_year = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

#CRUD - create, read, update,delete
# Student.objects.all()
# Student.objects.filter(age='18')
# s= Student(name='value' , age='value', course='value')
# s.save()

# s.age= 'valuee'
# s.save()
# s.delete()