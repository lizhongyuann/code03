from django.db import models

# Create your models here.

class Users(models.Model):

    username = models.CharField(max_length=20, verbose_name='用户名')
    passworld = models.CharField(max_length=128, verbose_name='密码')
    age = models.IntegerField(default=18, verbose_name='年龄')
    gender = models.BooleanField(default=False, verbose_name='性别')
    tel = models.CharField(max_length=20, verbose_name='电话')
    class Mata:
        db_table = 'db_users'
        verbose_name = '用户表'
