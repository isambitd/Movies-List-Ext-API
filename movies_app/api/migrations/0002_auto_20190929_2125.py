# Generated by Django 2.2.5 on 2019-09-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.CharField(max_length=50),
        ),
    ]
