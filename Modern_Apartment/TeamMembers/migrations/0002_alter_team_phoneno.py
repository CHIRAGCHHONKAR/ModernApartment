# Generated by Django 4.2.3 on 2023-09-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMembers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='PhoneNo',
            field=models.CharField(max_length=20),
        ),
    ]