# Generated by Django 2.1.7 on 2019-05-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190503_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_url1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_url2',
            field=models.CharField(default='', max_length=100),
        ),
    ]
