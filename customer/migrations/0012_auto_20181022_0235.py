# Generated by Django 2.1 on 2018-10-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20181021_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='r_phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='s_phone',
            field=models.CharField(max_length=50),
        ),
    ]
