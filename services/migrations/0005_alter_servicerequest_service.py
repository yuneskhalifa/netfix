# Generated by Django 5.1.2 on 2024-12-10 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_rename_hour_servicerequest_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='services.service'),
        ),
    ]
