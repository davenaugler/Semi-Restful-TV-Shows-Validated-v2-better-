# Generated by Django 2.2.5 on 2019-10-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(verbose_name='%B %m, %Y'),
        ),
    ]
