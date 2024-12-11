# Generated by Django 5.1.2 on 2024-12-08 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='field',
            field=models.CharField(choices=[('Air Conditioner', 'Air Conditioner'), ('All in One', 'All in One'), ('Carpentry', 'Carpentry'), ('Electricity', 'Electricity'), ('Gardening', 'Gardening'), ('Home Machines', 'Home Machines'), ('House Keeping', 'House Keeping'), ('Interior Design', 'Interior Design'), ('Locks', 'Locks'), ('Painting', 'Painting'), ('Plumbing', 'Plumbing'), ('Water Heaters', 'Water Heaters')], default='Air Conditioner', max_length=50),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]