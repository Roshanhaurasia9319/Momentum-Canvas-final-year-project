from django.db import models

# Create your models here.
class UserData(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=11)
    password=models.CharField(max_length=11)
    leetcode = models.CharField(max_length=500, blank=True, null=True)
    codechef = models.CharField(max_length=500, blank=True, null=True)
    geekforgeeks = models.CharField(max_length=500, blank=True, null=True)
    codeforces = models.CharField(max_length=500, blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
    