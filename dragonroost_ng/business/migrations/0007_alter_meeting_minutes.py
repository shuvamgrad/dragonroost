# Generated by Django 5.0.9 on 2024-10-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_alter_meeting_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='minutes',
            field=models.FileField(blank=True, upload_to='meetings/%Y'),
        ),
    ]
