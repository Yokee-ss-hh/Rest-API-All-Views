# Generated by Django 4.1.2 on 2022-11-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(related_name='courses', to='Api.student'),
        ),
    ]