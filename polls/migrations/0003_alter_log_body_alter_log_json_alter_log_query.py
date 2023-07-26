# Generated by Django 4.2.1 on 2023-07-26 13:09

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='json',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='query',
            field=models.TextField(null=True),
        ),
    ]