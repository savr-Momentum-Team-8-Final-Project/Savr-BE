# Generated by Django 3.2.6 on 2021-08-08 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expense_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='categoty',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
