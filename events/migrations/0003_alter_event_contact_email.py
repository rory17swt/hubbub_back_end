# Generated by Django 5.2.2 on 2025-06-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact_email',
            field=models.EmailField(max_length=100),
        ),
    ]
