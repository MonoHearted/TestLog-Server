# Generated by Django 2.1.5 on 2019-01-16 03:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nglogman', '0006_auto_20190115_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lgnode',
            name='nodeUUID',
            field=models.UUIDField(default=uuid.UUID('573f499b-7368-468e-96f0-f2ae89406851'), primary_key=True, serialize=False),
        ),
    ]