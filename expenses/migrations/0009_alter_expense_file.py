# Generated by Django 3.2.6 on 2021-08-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_alter_expense_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
