# Generated by Django 4.0.5 on 2022-06-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Token', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
