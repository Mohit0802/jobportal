# Generated by Django 4.2 on 2024-01-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=20),
        ),
    ]