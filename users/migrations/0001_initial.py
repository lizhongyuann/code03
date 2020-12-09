# Generated by Django 2.2.5 on 2020-12-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('passworld', models.CharField(max_length=128, verbose_name='密码')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('gender', models.BooleanField(default=False, verbose_name='性别')),
                ('tel', models.CharField(max_length=20, verbose_name='电话')),
            ],
        ),
    ]
