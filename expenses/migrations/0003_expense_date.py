# Generated by Django 3.2.6 on 2021-08-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expense_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]