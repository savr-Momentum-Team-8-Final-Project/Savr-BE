# Generated by Django 3.2.6 on 2021-08-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]