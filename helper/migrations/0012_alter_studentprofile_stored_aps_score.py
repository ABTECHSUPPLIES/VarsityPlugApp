# Generated by Django 5.1.6 on 2025-05-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0011_alter_university_minimum_aps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='stored_aps_score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
