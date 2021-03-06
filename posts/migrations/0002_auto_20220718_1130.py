# Generated by Django 3.2.14 on 2022-07-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
