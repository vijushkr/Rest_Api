from django.db import models
#Create your models here.
class Users(models.Model):
    name = models.CharField(max_length = 200,blank = False,default = '')
    age = models.IntegerField(blank = False,default = '')
    sex = models.CharField(max_length = 200,blank = False,default = '')
    bloodg = models.CharField(max_length = 200,blank = False,default = '')
    disease = models.CharField(max_length = 200,blank = False,default = '')