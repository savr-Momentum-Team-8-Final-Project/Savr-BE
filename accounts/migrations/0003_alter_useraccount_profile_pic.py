
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
