# Generated by Django 3.0.7 on 2020-06-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200628_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
