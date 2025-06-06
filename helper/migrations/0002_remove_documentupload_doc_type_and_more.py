# Generated by Django 5.2 on 2025-04-07 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentupload',
            name='doc_type',
        ),
        migrations.AddField(
            model_name='documentupload',
            name='document_type',
            field=models.CharField(choices=[('id', 'ID Document'), ('matric_results', 'Matric Results')], default='id', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documentupload',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png'])]),
        ),
    ]
