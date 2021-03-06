# Generated by Django 2.2.4 on 2019-08-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20190815_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyproduct',
            name='code',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='pyproduct',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pyproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]
