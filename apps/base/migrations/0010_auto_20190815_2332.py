# Generated by Django 2.2.4 on 2019-08-15 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20190815_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyproduct',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pyproduct',
            name='price',
            field=models.IntegerField(),
        ),
    ]
