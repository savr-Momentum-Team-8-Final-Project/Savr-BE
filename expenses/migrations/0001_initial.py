# Generated by Django 3.2.6 on 2021-08-07 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_title', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('note', models.TextField(blank=True)),
                ('categoty', models.CharField(choices=[('restaraunt', 'Restaraunt'), ('flight', 'Flight'), ('ticket', 'Ticket'), ('grocery', 'Grocery'), ('other', 'Other')], max_length=10)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
