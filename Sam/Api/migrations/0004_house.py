# Generated by Django 4.1.2 on 2022-11-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_delete_item_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('banner_name', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'housemodel',
            },
        ),
    ]
