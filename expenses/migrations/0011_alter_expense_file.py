# Generated by Django 3.2.6 on 2021-08-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_alter_expense_expense_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]