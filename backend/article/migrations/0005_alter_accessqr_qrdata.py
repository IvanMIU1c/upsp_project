# Generated by Django 4.1.4 on 2023-04-01 12:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_accesspending_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessqr',
            name='qrData',
            field=models.UUIDField(default=uuid.UUID('c3a3546c-9df3-4c47-a6e0-37a5bf3eb279'), editable=False, primary_key=True, serialize=False),
        ),
    ]
